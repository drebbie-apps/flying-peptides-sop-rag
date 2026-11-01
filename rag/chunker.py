"""Phase 4, step 3: structure-aware chunking by SOP section.

Usage (from the RAG_sys folder, venv active):  python rag\chunker.py
    Self-test: chunks the corpus, prints statistics, checks the rules below and compares
    with plain 512-character chunks. Exit code 1 if a check fails.
In code:  from chunker import chunk_corpus;  chunks = chunk_corpus(load_corpus())

Rules
1 Split each SOP on its section headings (##, ###, ####) first. A chunk never crosses a
  section or an SOP; heading lines are not part of the chunk text.
2 A section longer than CHUNK_SIZE characters is split by size with CHUNK_OVERLAP characters
  of overlap, preferring paragraph, line (table row), sentence and word boundaries.
  A piece that cannot stand alone (only table syntax such as a closing '|', or a table header
  without its rows) is merged into the next piece, else the previous one, within CHUNK_SIZE.
  A lone table header whose first row is too long to join it stays a chunk of its own
  (2 cases; repeating the header in each piece is a phase 5 refinement).
3 Each chunk text starts with a context line that is embedded with it, e.g.
  [TM-105 v2.0 Skyline data analysis · §7.2 Import and peak integration]
  CHUNK_SIZE limits the SOP text after this line (the line adds about 50 to 90 characters;
  with it a chunk stays well inside the 256-token input limit of all-MiniLM-L6-v2).
4 Metadata = the document metadata from the loader, plus: section ("7.2"; "0" for the title
  block before section 1), section_title, heading_path ("7 Procedure > 7.2 Import and peak
  integration"), steps (numbered steps in or continued into the chunk, "7.2.1, 7.2.2"; "none"
  if there are none), section_type ("admin" for Revision history, Approval and Document metadata,
  which are stored for the audit trail but not used for answers; "content" otherwise),
  chunk_id ("TM-105_v2.0_041"), chunk_index, chars (length of the SOP text).
Flying Peptides training case. Fictitious manufacturer: Positive Climb Diagnostics.
"""
import re
import sys
from pathlib import Path

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

CHUNK_SIZE = 512
CHUNK_OVERLAP = 51  # 10 % of CHUNK_SIZE
SEPARATORS = ["\n\n", "\n", ". ", "; ", ", ", " ", ""]
HEADING = re.compile(r"^(#{2,4}) (\d+(?:\.\d+)*) (.+)$", re.M)
ADMIN_SECTIONS = {"Revision history", "Approval", "Document metadata"}
STEP = re.compile(r"(?:^|\|)[ \t]*(\d+(?:\.\d+){2,})[ \t]", re.M)


def _splitter():
    return RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP,
                                          separators=SEPARATORS, keep_separator="end",
                                          add_start_index=True)


def sections(body):
    """Yield (number, title, heading_path, text) for each section of an SOP body."""
    heads = list(HEADING.finditer(body))
    first = heads[0].start() if heads else len(body)
    preamble = "\n".join(l for l in body[:first].split("\n") if not l.startswith("# ")).strip()
    if preamble:
        yield "0", "Title block", "0 Title block", preamble
    path = {}
    for i, h in enumerate(heads):
        level, number, title = len(h.group(1)), h.group(2), h.group(3).strip()
        path = {lv: t for lv, t in path.items() if lv < level}
        path[level] = f"{number} {title}"
        end = heads[i + 1].start() if i + 1 < len(heads) else len(body)
        text = body[h.end():end].strip()
        if text:  # a heading followed directly by a sub-heading has no text of its own
            yield number, title, " > ".join(path[lv] for lv in sorted(path)), text


def _steps(section, text, start, end):
    """Steps of this section that start inside [start, end), plus the step continued into it."""
    found = [(m.start(1), m.group(1)) for m in STEP.finditer(text)
             if m.group(1).startswith(section + ".")]
    before = [s for pos, s in found if pos < start]
    inside = [s for pos, s in found if start <= pos < end]
    newline = text.find("\n", start, end)
    first_line_end = end if newline == -1 else newline
    starts_new_step = any(start <= pos < first_line_end for pos, _ in found)
    steps = ([before[-1]] if before and not starts_new_step else []) + inside
    return ", ".join(dict.fromkeys(steps)) or "none"


ALNUM = re.compile(r"[A-Za-z0-9]")
TABLE_RULE = re.compile(r"^\|(\s*:?-+:?\s*\|)+$")


def _is_fragment(piece):
    """A size-split piece that cannot stand alone: no letters or digits (e.g. a lone '|'),
    or a table header whose rows went to the next piece."""
    return not ALNUM.search(piece) or bool(TABLE_RULE.match(piece.strip().split("\n")[-1]))


def _attach_back(text, out, frag):
    if out:
        s, _ = out[-1]
        joined = text[s:frag[0] + len(frag[1])]
        if len(joined) <= CHUNK_SIZE:
            out[-1] = (s, joined)
            return out
    if ALNUM.search(frag[1]):  # keep real content rather than lose it
        out.append(frag)
    return out  # a piece of table syntax only is dropped


def _merge_fragments(text, pieces):
    """Merge fragments into the next piece, else into the previous one, within CHUNK_SIZE."""
    out, carry = [], None
    for start, piece in pieces:
        if carry:
            joined = text[carry[0]:start + len(piece)]
            if len(joined) <= CHUNK_SIZE:
                start, piece = carry[0], joined
            else:
                out = _attach_back(text, out, carry)
            carry = None
        if _is_fragment(piece):
            carry = (start, piece)
            continue
        out.append((start, piece))
    if carry:
        out = _attach_back(text, out, carry)
    return out


def chunk_document(doc):
    meta, key = doc.metadata, doc.metadata["doc_key"]
    prefix = f"{meta['doc_id']}_v{meta['version']}"
    splitter, chunks = _splitter(), []
    for number, title, path, text in sections(doc.page_content):
        pieces = [(0, text)] if len(text) <= CHUNK_SIZE else _merge_fragments(text, [
            (p.metadata["start_index"], p.page_content) for p in splitter.create_documents([text])])
        for start, piece in pieces:
            n = len(chunks)
            chunks.append(Document(
                page_content=f"[{key} {meta['title']} · §{number} {title}]\n{piece}",
                metadata={**meta, "section": number, "section_title": title,
                          "heading_path": path,
                          "section_type": "admin" if path.split(" > ")[0].split(" ", 1)[-1]
                          in ADMIN_SECTIONS else "content",
                          "steps": _steps(number, text, start, start + len(piece)),
                          "chunk_id": f"{prefix}_{n:03d}", "chunk_index": n,
                          "chars": len(piece), "start_index": start}))
    return chunks


def chunk_corpus(docs):
    return [c for d in docs for c in chunk_document(d)]


def plain_chunks(docs):
    """Baseline for phase 5: plain 512-character chunks with no regard to sections."""
    splitter = _splitter()
    return [c for d in docs for c in splitter.create_documents([d.page_content], [d.metadata])]


def self_test():
    sys.path.insert(0, str(Path(__file__).parent))
    from loader import load_corpus
    docs = load_corpus()
    chunks = chunk_corpus(docs)
    problems = []

    print(f"{'doc_key':<13} {'sections':>8} {'split':>5} {'chunks':>6} {'mean':>5} {'max':>4}")
    for d in docs:
        cs = [c for c in chunks if c.metadata["doc_key"] == d.metadata["doc_key"]]
        secs = list(sections(d.page_content))
        sizes = [c.metadata["chars"] for c in cs]
        print(f"{d.metadata['doc_key']:<13} {len(secs):>8} "
              f"{sum(len(t) > CHUNK_SIZE for *_, t in secs):>5} {len(cs):>6} "
              f"{sum(sizes) // len(sizes):>5} {max(sizes):>4}")
        # Every character of every section is in at least one chunk (gaps may only be whitespace).
        for number, _, _, text in secs:
            covered = 0
            for c in (c for c in cs if c.metadata["section"] == number):
                s = c.metadata["start_index"]
                if re.sub(r"[\s|]", "", text[covered:s]):
                    problems.append(f"{d.metadata['doc_key']} §{number}: text lost before offset {s}")
                covered = max(covered, s + c.metadata["chars"])
            if re.sub(r"[\s|]", "", text[covered:]):
                problems.append(f"{d.metadata['doc_key']} §{number}: text lost at the end")
    print(f"{len(chunks)} chunks in total; CHUNK_SIZE {CHUNK_SIZE}, CHUNK_OVERLAP {CHUNK_OVERLAP}.")
    n_admin = sum(c.metadata["section_type"] == "admin" for c in chunks)
    print(f"Admin chunks (Revision history, Approval, Document metadata): {n_admin}")
    if not 0 < n_admin < len(chunks):
        problems.append(f"section_type: {n_admin} admin chunks of {len(chunks)}")
    headers = [c.metadata["chunk_id"] for c in chunks
               if _is_fragment(c.page_content.split("\n", 1)[1])]
    print(f"Table headers that could not be merged with their first row (row too long): "
          f"{len(headers)} {headers if headers else ''}")

    ids = [c.metadata["chunk_id"] for c in chunks]
    if len(set(ids)) != len(ids):
        problems.append("chunk_id not unique")
    for c in chunks:
        m, body = c.metadata, c.page_content.split("\n", 1)[1]
        if m["chars"] > CHUNK_SIZE:
            problems.append(f"{m['chunk_id']}: {m['chars']} characters > {CHUNK_SIZE}")
        if re.search(r"^#{1,6} ", body, re.M):
            problems.append(f"{m['chunk_id']}: contains a heading line (crosses a section)")
        if not ALNUM.search(body):
            problems.append(f"{m['chunk_id']}: no content (table syntax only)")
        if not c.page_content.startswith(f"[{m['doc_key']} "):
            problems.append(f"{m['chunk_id']}: context line missing")
        bad = [k for k, v in m.items() if not isinstance(v, (str, int, float, bool))]
        if bad:
            problems.append(f"{m['chunk_id']}: metadata not storable in Chroma: {bad}")

    # Spot checks that later steps depend on.
    ncr = [c for c in chunks if c.metadata["doc_key"] == "QMS-003 v1.0"
           and c.metadata["section"] == "7.1" and "7.1.1" in c.metadata["steps"].split(", ")]
    if not ncr or "within 1 working day" not in ncr[0].page_content:
        problems.append("QMS-003 v1.0 §7.1.1 (raise the NCR within 1 working day) not found as a step")
    if any(c.metadata["status"] != "Superseded" for c in chunks
           if c.metadata["doc_key"] == "TM-105 v1.0"):
        problems.append("a TM-105 v1.0 chunk lost its Superseded status")
    if not any("26.1" in c.page_content for c in chunks if c.metadata["doc_key"] == "TM-105 v2.0"):
        problems.append("no TM-105 v2.0 chunk mentions Skyline 26.1")

    # Comparison with plain chunks (phase 5 baseline).
    plain = plain_chunks(docs)
    crossing = sum(bool(re.search(r"^#{2,4} ", p.page_content[1:], re.M)) for p in plain)
    print(f"Plain baseline: {len(plain)} chunks, {crossing} of them run across a section heading.")

    example = ncr[0] if ncr else chunks[0]
    print("\nExample chunk:", {k: example.metadata[k] for k in
                                ("chunk_id", "section", "heading_path", "steps", "chars")})
    print(example.page_content)
    print()
    for p in problems:
        print(f"FAIL  {p}")
    print("Chunking checks passed." if not problems else "Chunking checks failed.")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(self_test())
