"""Phase 4, step 2: load the clean SOP corpus with its front matter as metadata.

Usage (from the RAG_sys folder, venv active):  python rag\loader.py
    Self-test: loads every SOP, prints one line per document and checks the metadata
    against master_document_list.csv. Exit code 1 if a check fails.
In code:  from loader import load_corpus;  docs = load_corpus()

Each SOP becomes one LangChain Document:
  page_content = the Markdown body (front matter removed, headings and section numbers kept)
  metadata     = the 17 front matter fields, flattened so Chroma can store and filter them
                 (str, int, float or bool only: dates as ISO text, null as "none",
                 iso_clause list as "4.1.6, 8.3"), plus:
                 doc_key  "TM-105 v2.0"  (used in citations: [TM-105 v2.0 §7.2])
                 file     the file name in SOPs/clean
The loader reads every status, including Superseded: the status filter is applied at
retrieval (step 4), so superseded versions stay in the store for the audit trail.
Flying Peptides training case. Fictitious manufacturer: Positive Climb Diagnostics.
"""
import csv
import datetime
import re
import sys
from pathlib import Path

import yaml
from langchain_core.documents import Document

RAG_SYS = Path(__file__).resolve().parent.parent
CORPUS = RAG_SYS / "SOPs" / "clean"
FIELDS = ["doc_id", "doc_type", "title", "manufacturer", "assay", "source", "version",
          "status", "approval_date", "effective_date", "supersedes", "superseded_by",
          "iso_clause", "author", "reviewer", "approver", "training_case"]
STATUSES = {"Draft", "Approved", "Effective", "Superseded", "Withdrawn"}
FRONT_MATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)


class CorpusError(ValueError):
    pass


def flat(value):
    """Front matter value -> a type Chroma accepts as metadata."""
    if value is None:
        return "none"
    if isinstance(value, (datetime.date, datetime.datetime)):
        return value.isoformat()
    if isinstance(value, list):
        return ", ".join(str(v) for v in value)
    if isinstance(value, (str, int, float, bool)):
        return value
    raise CorpusError(f"unsupported metadata type {type(value).__name__}")


def load_sop(path):
    text = path.read_text(encoding="utf-8")
    m = FRONT_MATTER.match(text)
    if not m:
        raise CorpusError(f"{path.name}: no YAML front matter")
    fm = yaml.safe_load(m.group(1))
    missing = [f for f in FIELDS if f not in fm]
    extra = [f for f in fm if f not in FIELDS]
    if missing or extra:
        raise CorpusError(f"{path.name}: missing fields {missing}, unexpected fields {extra}")
    if fm["status"] not in STATUSES:
        raise CorpusError(f"{path.name}: status {fm['status']!r} is not a controlled value")
    if not isinstance(fm["version"], str):
        raise CorpusError(f"{path.name}: version must be quoted text, got {fm['version']!r}")
    body = text[m.end():].strip()
    if not body:
        raise CorpusError(f"{path.name}: empty body")
    metadata = {f: flat(fm[f]) for f in FIELDS}
    metadata["doc_key"] = f"{fm['doc_id']} v{fm['version']}"
    metadata["file"] = path.name
    return Document(page_content=body, metadata=metadata)


def load_corpus(folder=CORPUS):
    paths = sorted(Path(folder).glob("*.md"))
    if not paths:
        raise CorpusError(f"no .md files in {folder}")
    docs = [load_sop(p) for p in paths]
    keys = [d.metadata["doc_key"] for d in docs]
    dupes = {k for k in keys if keys.count(k) > 1}
    if dupes:
        raise CorpusError(f"duplicate doc_id + version: {sorted(dupes)}")
    effective = [d.metadata["doc_id"] for d in docs if d.metadata["status"] == "Effective"]
    multi = {i for i in effective if effective.count(i) > 1}
    if multi:
        raise CorpusError(f"more than one Effective version of {sorted(multi)}")
    return docs


def self_test():
    try:
        docs = load_corpus()
    except CorpusError as e:
        print(f"FAIL  {e}")
        return 1
    print(f"{'doc_key':<13} {'status':<11} {'effective':<11} {'chars':>6}  file")
    for d in docs:
        m = d.metadata
        print(f"{m['doc_key']:<13} {m['status']:<11} {m['effective_date']:<11} "
              f"{len(d.page_content):>6}  {m['file']}")
    problems = []
    with open(CORPUS / "master_document_list.csv", encoding="utf-8-sig", newline="") as f:
        rows = {r["file"]: r for r in csv.DictReader(f)}
    for d in docs:
        m, row = d.metadata, rows.get(d.metadata["file"])
        if row is None:
            problems.append(f"{m['file']}: not in master_document_list.csv")
            continue
        for field in FIELDS:
            if str(m[field]).lower() != row[field].lower():
                problems.append(f"{m['file']}: {field} = {m[field]!r}, master list has {row[field]!r}")
        if not d.page_content.startswith(f"# {m['doc_id']}"):
            problems.append(f"{m['file']}: body does not start with the '# {m['doc_id']}' title")
    if len(rows) != len(docs):
        problems.append(f"master list has {len(rows)} rows, corpus has {len(docs)} files")
    bad_types = {k for d in docs for k, v in d.metadata.items()
                 if not isinstance(v, (str, int, float, bool))}
    if bad_types:
        problems.append(f"metadata not storable in Chroma: {sorted(bad_types)}")
    print(f"{len(docs)} documents, {len(docs[0].metadata)} metadata fields each.")
    for p in problems:
        print(f"FAIL  {p}")
    print("Loader checks passed." if not problems else "Loader checks failed.")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(self_test())
