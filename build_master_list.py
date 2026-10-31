"""Build the master document list from the YAML front matter of the SOP Markdown files.

Usage:  python build_master_list.py [corpus_folder]     (default: SOPs/clean next to this script)
Output: master_document_list.csv in the corpus folder (UTF-8 with BOM, opens directly in Excel).
Checks: every file has all fields; status is a controlled value; effective_date = approval_date + 14 days
        (QMS-001 §6.5.1); at most one Effective version per doc_id; supersedes / superseded_by match.
Flying Peptides training case. Fictitious manufacturer: Positive Climb Diagnostics.
"""
import csv, datetime, sys
from pathlib import Path
import yaml

FIELDS = ["doc_id", "version", "title", "doc_type", "status", "approval_date", "effective_date",
          "supersedes", "superseded_by", "source", "assay", "iso_clause", "manufacturer",
          "author", "reviewer", "approver", "training_case"]
STATUSES = {"Draft", "Approved", "Effective", "Superseded", "Withdrawn"}

def front_matter(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path.name}: no YAML front matter")
    return yaml.safe_load(text.split("---\n", 2)[1])

def vkey(v):
    major, minor = v.split(".")
    return int(major), int(minor)

def main():
    folder = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent / "SOPs" / "clean"
    rows, problems = [], []
    for path in sorted(folder.glob("*.md")):
        fm = front_matter(path)
        missing = [f for f in FIELDS if f not in fm]
        if missing:
            problems.append(f"{path.name}: missing {missing}")
        if fm.get("status") not in STATUSES:
            problems.append(f"{path.name}: status '{fm.get('status')}' not allowed")
        a, e = fm.get("approval_date"), fm.get("effective_date")
        if isinstance(a, datetime.date) and isinstance(e, datetime.date) and e - a != datetime.timedelta(days=14):
            problems.append(f"{path.name}: effective_date is approval_date + {(e - a).days} days, not 14")
        fm["file"] = path.name
        rows.append(fm)

    rows.sort(key=lambda r: (r["doc_id"], vkey(r["version"])))
    ids = {f"{r['doc_id']} v{r['version']}": r for r in rows}
    for r in rows:
        name = f"{r['doc_id']} v{r['version']}"
        if [x["status"] for x in rows if x["doc_id"] == r["doc_id"]].count("Effective") > 1:
            problems.append(f"{r['doc_id']}: more than one Effective version")
        if r.get("supersedes") and ids.get(r["supersedes"], {}).get("superseded_by") != name:
            problems.append(f"{name} supersedes {r['supersedes']}, but that file does not say superseded_by {name}")
        if r.get("superseded_by") and ids.get(r["superseded_by"], {}).get("supersedes") != name:
            problems.append(f"{name} is superseded_by {r['superseded_by']}, but that file does not say supersedes {name}")

    out = folder / "master_document_list.csv"
    with out.open("w", newline="", encoding="utf-8-sig") as fh:
        w = csv.writer(fh)
        w.writerow(FIELDS + ["file"])
        for r in rows:
            cells = []
            for f in FIELDS + ["file"]:
                v = r.get(f)
                if v is None:
                    v = "none"
                elif isinstance(v, list):
                    v = ", ".join(v)
                elif isinstance(v, bool):
                    v = "true" if v else "false"
                cells.append(str(v))
            w.writerow(cells)
    print(f"Wrote {out} with {len(rows)} documents.")
    for p in sorted(set(problems)):
        print("CHECK FAILED:", p)
    if not problems:
        print("All checks passed.")
    return 1 if problems else 0

if __name__ == "__main__":
    sys.exit(main())
