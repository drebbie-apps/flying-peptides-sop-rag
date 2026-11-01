"""Phase 4, step 5: grounded answers from the Effective SOPs, with SOP-level citations.

Usage (from the RAG_sys folder, venv active; build the store first with python rag\store.py):
    python rag\answer.py                 self-test with the end-of-phase test questions
    python rag\answer.py "question"      answer one question
In code:  from answer import answer;  result = answer("Which Skyline version do we use?")

How an answer is made
1 retrieve() returns the top K = 8 chunks with status = Effective and section_type = content.
2 Chunks with a cosine distance above MAX_DISTANCE are dropped as too weak. If none is left,
  the reply is NOT_COVERED and the model is not called.
3 The model gets the question, the remaining chunks as numbered excerpts with their citation
  label, and the register of Effective SOPs (doc_key, title, approval and effective dates).
  The system prompt allows only what the excerpts say, a citation after every statement, and
  NOT_COVERED when the excerpts do not answer the question.
4 Every citation in the reply is checked against the excerpts: it must name an excerpt's
  doc_key, and its section must be that excerpt's section or a step in it. A reply with no
  valid citation, or with a citation that matches no excerpt, is flagged.
Model: ANTHROPIC_MODEL environment variable (default claude-sonnet-5-5). No sampling settings
(anthropic SDK 2.x does not accept temperature); consistency comes from the fixed prompt and
the citation check.
The API key is read from ANTHROPIC_API_KEY only.
Flying Peptides training case. Fictitious manufacturer: Positive Climb Diagnostics.
"""
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from loader import load_corpus  # noqa: E402
from store import K, retrieve  # noqa: E402

MODEL = os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-5-5")
MAX_DISTANCE = 0.75  # relevant chunks scored 0.33-0.66 in the 1-Nov-2026 store run
NOT_COVERED = "Not covered by the effective SOPs."
CITATION = re.compile(r"([A-Z]+-\d+) v(\d+\.\d+) §(\d+(?:\.\d+)*)")

SYSTEM = f"""You answer questions from staff of Positive Climb Diagnostics (a fictitious \
manufacturer in a training case) about its standard operating procedures (SOPs).

Rules:
1. Use only the SOP excerpts and the SOP register given in the user message. Do not use \
outside knowledge, and do not add values, versions, limits or steps that the excerpts do not state.
2. Cite every statement in square brackets right after it: [DOC-ID vX.Y §section], or the \
numbered step when the excerpt shows one, e.g. [QMS-003 v1.0 §7.1.1]. Copy the document ID \
and version exactly from the excerpt label. Several sources go in one bracket, separated by "; ".
3. When an excerpt only refers to a rule in another SOP (for example "the time limit of \
QMS-003 §7.1.1") and the excerpt from that other SOP is given, cite the SOP that states the rule.
4. If the excerpts do not answer the question, reply with exactly: {NOT_COVERED}
   If they answer only part of it, answer that part and then say which part is {NOT_COVERED[0].lower() + NOT_COVERED[1:-1]}.
5. Keep the answer short and direct: the answer first, then any condition or responsibility \
that belongs to it. Use the SOP wording for limits and units. No preamble."""


def register():
    rows = [d.metadata for d in load_corpus() if d.metadata["status"] == "Effective"]
    return "\n".join(f"- {m['doc_key']}: {m['title']} ({m['doc_type']}), approved "
                     f"{m['approval_date']}, effective {m['effective_date']}"
                     f"{', supersedes ' + m['supersedes'] if m['supersedes'] != 'none' else ''}"
                     for m in rows)


def build_prompt(question, hits):
    parts = []
    for i, h in enumerate(hits, 1):
        steps = f' steps="{h["steps"]}"' if h["steps"] != "none" else ""
        parts.append(f'<excerpt n="{i}" cite="{h["doc_key"]} §{h["section"]}"{steps}>\n'
                     f'{h["text"]}\n</excerpt>')
    excerpts = "\n\n".join(parts)
    return (f"<sop_register>\nEffective SOPs:\n{register()}\n</sop_register>\n\n"
            f"<excerpts>\n{excerpts}\n</excerpts>\n\n<question>{question}</question>")


def check_citations(reply, hits):
    """Return (valid, invalid) citation strings found in the reply."""
    valid, invalid = [], []
    for doc, ver, sec in CITATION.findall(reply):
        key, label = f"{doc} v{ver}", f"{doc} v{ver} §{sec}"
        ok = any(h["doc_key"] == key and (sec == h["section"] or sec.startswith(h["section"] + "."))
                 for h in hits)
        (valid if ok else invalid).append(label)
    return list(dict.fromkeys(valid)), list(dict.fromkeys(invalid))


def call_claude(system, prompt):
    import anthropic
    resp = anthropic.Anthropic().messages.create(
        model=MODEL, max_tokens=700, system=system,
        messages=[{"role": "user", "content": prompt}])
    return "".join(b.text for b in resp.content if b.type == "text").strip()


def answer(question, llm=call_claude, collection=None):
    all_hits = retrieve(question, collection=collection)
    hits = [h for h in all_hits if h["distance"] <= MAX_DISTANCE]
    result = {"question": question, "hits": hits, "best_distance":
              all_hits[0]["distance"] if all_hits else None}
    if not hits:
        result.update(reply=NOT_COVERED, called_model=False, valid=[], invalid=[], flags=[])
        return result
    reply = llm(SYSTEM, build_prompt(question, hits))
    valid, invalid = check_citations(reply, hits)
    flags = []
    if reply != NOT_COVERED and not valid:
        flags.append("no valid citation")
    if invalid:
        flags.append(f"citation not in the excerpts: {', '.join(invalid)}")
    result.update(reply=reply, called_model=True, valid=valid, invalid=invalid, flags=flags)
    return result


def show(r):
    print(f"\nQ: {r['question']}")
    print(f"   {len(r['hits'])} of {K} retrieved chunks within distance {MAX_DISTANCE} "
          f"(best {r['best_distance']}); model called: {r['called_model']}")
    print("A: " + r["reply"].replace("\n", "\n   "))
    print(f"   citations checked: {', '.join(r['valid']) or 'none'}")
    for f in r["flags"]:
        print(f"   FLAG {f}")


# (question, text the reply must contain, pattern it must not match, citation it must include)
TESTS = [
    ("Which Skyline version do we use?", "26.1", r"(?i)(?:\bv|version\s*|skyline\s*)3\.6(?!\d)",
     "TM-105 v2.0 §"),
    ("How quickly must an NCR be raised?", "1 working day", None, "QMS-003 v1.0 §7.1"),
    ("What is the travel expense limit for conference trips?", NOT_COVERED, None, None),
]


def self_test(llm=call_claude, collection=None):
    problems = []
    for question, must, must_not, cite in TESTS:
        r = answer(question, llm, collection)
        show(r)
        if must and must not in r["reply"]:
            problems.append(f"'{question}': reply lacks '{must}'")
        if must_not and re.search(must_not, r["reply"]):
            problems.append(f"'{question}': reply names the superseded Skyline v3.6")
        if cite and not any(v.startswith(cite) for v in r["valid"]):
            problems.append(f"'{question}': no valid citation starting with '{cite}'")
        problems += [f"'{question}': {f}" for f in r["flags"]]
    print()
    for p in problems:
        print(f"FAIL  {p}")
    print("Answer checks passed." if not problems else "Answer checks failed.")
    return 1 if problems else 0


if __name__ == "__main__":
    if len(sys.argv) > 1:
        show(answer(" ".join(sys.argv[1:])))
    else:
        sys.exit(self_test())
