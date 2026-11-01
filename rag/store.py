"""Phase 4, step 4: embed the chunks, store them in Chroma and retrieve only Effective SOPs.

Usage (from the RAG_sys folder, venv active):
    python rag\store.py                 rebuild the store from SOPs/clean and run the self-test
    python rag\store.py "question"      retrieve the top chunks for a question (Effective only)
    python rag\store.py --all "question"   same, all chunks (audit view; never used for answers)
In code:  from store import retrieve;  hits = retrieve("Which Skyline version do we use?")

Store: persistent Chroma database in RAG_sys/chroma_store (kept out of Git; rebuilt from the
corpus at any time). One collection "sop_chunks", cosine distance, embeddings from Chroma's
built-in local model all-MiniLM-L6-v2. Every chunk is stored, Superseded ones included, so the
store keeps the audit trail. retrieve() returns the top K = 8 chunks with status = Effective and
section_type = content unless told otherwise, so a superseded version is never returned for an
answer, and revision history, approval and metadata rows do not crowd out the procedure text. The collection metadata records when and
from which Git commit of the corpus the store was built, and the chunking settings.
Flying Peptides training case. Fictitious manufacturer: Positive Climb Diagnostics.
"""
import datetime
import os
import subprocess
import sys
from pathlib import Path

import chromadb
from chromadb.config import Settings

sys.path.insert(0, str(Path(__file__).parent))
from chunker import CHUNK_OVERLAP, CHUNK_SIZE, chunk_corpus  # noqa: E402
from loader import RAG_SYS, load_corpus  # noqa: E402

STORE_DIR = Path(os.environ.get("RAG_STORE_DIR", RAG_SYS / "chroma_store"))
COLLECTION = "sop_chunks"
EMBEDDING_MODEL = "all-MiniLM-L6-v2 (Chroma built-in, local ONNX)"
K = 8  # chunks retrieved for an answer


def _client(path=None):
    return chromadb.PersistentClient(path=str(path or STORE_DIR),
                                     settings=Settings(anonymized_telemetry=False))


def _corpus_commit():
    try:
        out = subprocess.run(["git", "-C", str(RAG_SYS), "log", "-1", "--format=%h",
                              "--", "SOPs/clean"], capture_output=True, text=True, timeout=10)
        return out.stdout.strip() or "unknown"
    except (OSError, subprocess.SubprocessError):
        return "unknown"


def build_store(path=None, embedding_function=None):
    """Delete and rebuild the collection from the corpus. Returns the collection."""
    client = _client(path)
    try:
        client.delete_collection(COLLECTION)
    except Exception:  # the collection does not exist yet
        pass
    chunks = chunk_corpus(load_corpus())
    kwargs = {"embedding_function": embedding_function} if embedding_function else {}
    col = client.create_collection(
        COLLECTION, configuration={"hnsw": {"space": "cosine"}},
        metadata={"built_at": datetime.datetime.now().isoformat(timespec="seconds"),
                  "corpus_commit": _corpus_commit(), "embedding_model": EMBEDDING_MODEL,
                  "chunk_size": CHUNK_SIZE, "chunk_overlap": CHUNK_OVERLAP,
                  "chunks": len(chunks)},
        **kwargs)
    for i in range(0, len(chunks), 200):
        batch = chunks[i:i + 200]
        col.add(ids=[c.metadata["chunk_id"] for c in batch],
                documents=[c.page_content for c in batch],
                metadatas=[c.metadata for c in batch])
    return col


def get_collection(path=None, embedding_function=None):
    kwargs = {"embedding_function": embedding_function} if embedding_function else {}
    return _client(path).get_collection(COLLECTION, **kwargs)


def retrieve(question, k=K, status="Effective", content_only=True, collection=None):
    """Top-k chunks for a question: Effective content chunks by default.
    status=None and content_only=False give the audit view (all chunks); never used for answers."""
    col = collection or get_collection()
    conditions = ([{"status": status}] if status else []) + (
        [{"section_type": "content"}] if content_only else [])
    where = (conditions[0] if len(conditions) == 1
             else {"$and": conditions} if conditions else None)
    res = col.query(query_texts=[question], n_results=k, where=where,
                    include=["documents", "metadatas", "distances"])
    return [{"chunk_id": m["chunk_id"], "doc_key": m["doc_key"], "status": m["status"],
             "section": m["section"], "section_type": m["section_type"], "steps": m["steps"],
             "distance": round(d, 3), "text": doc}
            for doc, m, d in zip(res["documents"][0], res["metadatas"][0], res["distances"][0])]


def show(hits):
    for h in hits:
        first = h["text"].split("\n", 1)[1][:110].replace("\n", " ")
        print(f"  {h['distance']:.3f}  {h['doc_key']:<13} {h['status']:<10} §{h['section']:<5} "
              f"steps {h['steps']:<16} {first}")


TEST_QUESTIONS = [
    ("Which Skyline version do we use?", "TM-105 v2.0", "26.1"),
    ("How quickly must an NCR be raised?", "QMS-003 v1.0", "within 1 working day"),
    ("What is the signal-to-noise acceptance criterion for a peak?", "TM-105 v2.0", "S/N"),
    ("What must be checked in the system suitability test before a run?", "TM-104 v1.0", None),
]


def self_test(path=None, embedding_function=None):
    col = build_store(path, embedding_function)
    problems, warnings = [], []
    meta = col.metadata
    print(f"Store: {path or STORE_DIR}")
    print(f"Built {meta['built_at']} from corpus commit {meta['corpus_commit']}, "
          f"{meta['embedding_model']}, {meta['chunks']} chunks.")

    # 1 Everything is stored, the superseded version included.
    total = col.count()
    by_doc = {}
    for m in col.get(include=["metadatas"])["metadatas"]:
        by_doc.setdefault((m["doc_key"], m["status"]), 0)
        by_doc[(m["doc_key"], m["status"])] += 1
    for (key, status), n in sorted(by_doc.items()):
        print(f"  stored  {key:<13} {status:<10} {n:>4} chunks")
    if total != meta["chunks"]:
        problems.append(f"store holds {total} chunks, expected {meta['chunks']}")
    if ("TM-105 v1.0", "Superseded") not in by_doc:
        problems.append("TM-105 v1.0 is not in the store (audit trail incomplete)")

    # 2 The filter: asking for every answerable chunk returns no other status or section type.
    all_meta = col.get(include=["metadatas"])["metadatas"]
    n_ok = sum(m["status"] == "Effective" and m["section_type"] == "content" for m in all_meta)
    n_admin = sum(m["section_type"] == "admin" for m in all_meta)
    everything = retrieve("Skyline version", k=n_ok, collection=col)
    leaked = [h["chunk_id"] for h in everything
              if h["status"] != "Effective" or h["section_type"] != "content"]
    if leaked or len(everything) != n_ok:
        problems.append(f"filter returned {len(everything)} of {n_ok} chunks; "
                        f"not Effective content: {leaked[:5]}")
    else:
        print(f"Filter: all {n_ok} Effective content chunks returned, 0 Superseded, "
              f"0 of the {n_admin} admin chunks.")

    # 3 Test questions: filtered retrieval, plus the unfiltered audit view for the trap.
    for question, want_doc, want_text in TEST_QUESTIONS:
        hits = retrieve(question, collection=col)
        print(f"\nQ: {question}")
        show(hits)
        if any(h["status"] != "Effective" or h["section_type"] != "content" for h in hits):
            problems.append(f"'{question}': a Superseded or admin chunk was returned")
        rank = next((i + 1 for i, h in enumerate(hits) if h["doc_key"] == want_doc
                     and (not want_text or want_text in h["text"])), None)
        if rank is None:
            warnings.append(f"'{question}': no {want_doc} chunk"
                            f"{' with ' + repr(want_text) if want_text else ''} in the top {K}")
        else:
            print(f"  -> expected source ({want_doc}) at rank {rank}")
    trap = retrieve(TEST_QUESTIONS[0][0], status=None, content_only=False, collection=col)
    n_old = sum(h["doc_key"] == "TM-105 v1.0" for h in trap)
    print(f"\nWithout the filters (audit view), the top {K} for '{TEST_QUESTIONS[0][0]}' "
          f"hold {n_old} TM-105 v1.0 chunk(s):")
    show(trap)

    print()
    for w in warnings:
        print(f"WARN  {w}")
    for p in problems:
        print(f"FAIL  {p}")
    print("Store checks passed." if not problems else "Store checks failed.")
    return 1 if problems else 0


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        sys.exit(self_test())
    status = "Effective"
    content_only = True
    if args[0] == "--all":
        status, content_only, args = None, False, args[1:]
    show(retrieve(" ".join(args), status=status, content_only=content_only))
