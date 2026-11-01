"""Phase 5: retrieval hit rate on the gold question set (no model calls, no API cost).

Usage (from the RAG_sys folder, venv active; store built with python rag\store.py):
    python eval\hit_rate.py --label baseline          k = K from rag/store.py (8)
    python eval\hit_rate.py --label k5 --k 5          another k
Each run is logged: one summary row appended to eval/runs/retrieval_runs.csv and one detail
file eval/runs/retrieval_<timestamp>_<label>.csv. Commit both, so every tuning step has evidence.

Scoring (answerable questions: single, cross, trap)
  An expected source "TM-104 v1.0 §7.5" is found when a retrieved chunk has that doc_key and
  that section (or a subsection of it, e.g. §7.5.1).
  hit         at least one expected source is in the top k        (Masterplan definition)
  all found   every expected source is in the top k               (stricter, for cross questions)
  usable      the found chunk also has a distance <= MAX_DISTANCE of rag/answer.py, so the
              answer step keeps it (a hit that the cut-off drops cannot be used for the answer)
  rank        rank of the first chunk that matches an expected source
Unanswerable questions: no expected source. Reported: best distance. Above MAX_DISTANCE the
answer step replies "not covered" without the model; below it, the model has to decide.
Superseded chunks: counted over all questions; must be 0 (the status filter).
Flying Peptides training case. Fictitious manufacturer: Positive Climb Diagnostics.
"""
import argparse
import csv
import datetime
import re
import subprocess
import sys
from pathlib import Path

EVAL = Path(__file__).resolve().parent
RAG_SYS = EVAL.parent
sys.path.insert(0, str(RAG_SYS / "rag"))
from answer import MAX_DISTANCE  # noqa: E402
from store import K, get_collection, retrieve  # noqa: E402

GOLD = EVAL / "gold_questions.csv"
RUNS = EVAL / "runs"
SOURCE = re.compile(r"^([A-Z]+-\d+ v\d+\.\d+) §(\d+(?:\.\d+)*)$")


def load_gold(path=GOLD):
    with open(path, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        r["sources"] = []
        if r["expected_sources"].strip().lower() != "none":
            for s in r["expected_sources"].split(";"):
                m = SOURCE.match(s.strip())
                if not m:
                    raise ValueError(f"{r['id']}: cannot read expected source {s!r}")
                r["sources"].append((m.group(1), m.group(2)))
    return rows


def matches(hit, source):
    key, section = source
    return hit["doc_key"] == key and (hit["section"] == section
                                      or hit["section"].startswith(section + "."))


def score(row, hits):
    found = {}
    for source in row["sources"]:
        rank = next((i for i, h in enumerate(hits, 1) if matches(h, source)), None)
        if rank:
            found[source] = (rank, hits[rank - 1]["distance"])
    first = min(found.values()) if found else None
    return {
        "id": row["id"], "type": row["type"], "question": row["question"],
        "expected": row["expected_sources"],
        "hit": bool(found) if row["sources"] else "",
        "all_found": len(found) == len(row["sources"]) if row["sources"] else "",
        "usable": (first[1] <= MAX_DISTANCE) if first else ("" if not row["sources"] else False),
        "rank": first[0] if first else "",
        "found_distance": first[1] if first else "",
        "best_distance": hits[0]["distance"] if hits else "",
        "superseded_returned": sum(h["status"] != "Effective" for h in hits),
        "top_k": "; ".join(f"{h['doc_key']} §{h['section']} ({h['distance']:.3f})" for h in hits),
    }


def git(*args):
    try:
        out = subprocess.run(["git", "-C", str(RAG_SYS), *args], capture_output=True,
                             text=True, timeout=10)
        return out.stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return ""


def run(label, k=K, collection=None, runs_dir=RUNS):
    col = collection or get_collection()
    gold = load_gold()
    results = [score(r, retrieve(r["question"], k=k, collection=col)) for r in gold]
    answerable = [r for r in results if r["hit"] != ""]
    unanswerable = [r for r in results if r["hit"] == ""]

    print(f"Gold set: {len(gold)} questions ({len(answerable)} answerable, "
          f"{len(unanswerable)} unanswerable); k = {k}; MAX_DISTANCE = {MAX_DISTANCE}")
    print(f"Store: built {col.metadata.get('built_at')}, corpus commit "
          f"{col.metadata.get('corpus_commit')}, {col.metadata.get('chunks')} chunks\n")
    print(f"{'id':<4} {'type':<12} {'hit':<4} {'all':<4} {'usable':<6} {'rank':>4} "
          f"{'dist':>6}  expected")
    for r in results:
        if r["hit"] == "":
            print(f"{r['id']:<4} {r['type']:<12} {'-':<4} {'-':<4} {'-':<6} {'-':>4} "
                  f"{r['best_distance']:>6.3f}  none: best distance "
                  f"{'above' if r['best_distance'] > MAX_DISTANCE else 'BELOW'} the cut-off")
        else:
            yn = lambda v: "yes" if v else "NO"  # noqa: E731
            dist = f"{r['found_distance']:.3f}" if r["found_distance"] != "" else "-"
            print(f"{r['id']:<4} {r['type']:<12} {yn(r['hit']):<4} {yn(r['all_found']):<4} "
                  f"{yn(r['usable']):<6} {str(r['rank'] or '-'):>4} {dist:>6}  {r['expected']}")
            if not r["all_found"]:
                print(f"       top {k}: {r['top_k']}")

    n = len(answerable)
    hits = sum(r["hit"] for r in answerable)
    all_found = sum(r["all_found"] for r in answerable)
    usable = sum(r["usable"] for r in answerable)
    ranks = [r["rank"] for r in answerable if r["rank"]]
    mrr = sum(1 / r["rank"] if r["rank"] else 0 for r in answerable) / n
    refused = sum(r["best_distance"] > MAX_DISTANCE for r in unanswerable)
    superseded = sum(r["superseded_returned"] for r in results)
    print(f"\nHit rate@{k}: {hits}/{n} = {hits / n:.0%}   all sources found: {all_found}/{n}   "
          f"usable after the cut-off: {usable}/{n}")
    print(f"Mean reciprocal rank: {mrr:.2f}   ranks of first match: {ranks}")
    print(f"Unanswerable refused by the cut-off alone: {refused}/{len(unanswerable)} "
          f"(the rest depend on the model)")
    print(f"Superseded chunks returned: {superseded}" + ("" if superseded == 0 else "  FAIL"))

    # Log the run.
    stamp = datetime.datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    safe = re.sub(r"[^A-Za-z0-9_-]+", "-", label).strip("-") or "run"
    runs_dir.mkdir(exist_ok=True)
    detail = runs_dir / f"retrieval_{stamp}_{safe}.csv"
    with open(detail, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(results[0]))
        w.writeheader()
        w.writerows(results)
    summary = runs_dir / "retrieval_runs.csv"
    new = not summary.exists()
    dirty = " (uncommitted changes)" if git("status", "--porcelain", "--", "rag", "SOPs/clean",
                                 "eval/gold_questions.csv", "eval/hit_rate.py") else ""
    with open(summary, "a", encoding="utf-8-sig" if new else "utf-8", newline="") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["run_at", "label", "code_commit", "corpus_commit", "store_built_at",
                        "chunks", "chunk_size", "chunk_overlap", "k", "max_distance",
                        "answerable", "hit_rate", "all_found", "usable", "mrr",
                        "unanswerable_refused", "superseded_returned", "detail_file"])
        w.writerow([stamp, label, git("rev-parse", "--short", "HEAD") + dirty,
                    col.metadata.get("corpus_commit"), col.metadata.get("built_at"),
                    col.metadata.get("chunks"), col.metadata.get("chunk_size"),
                    col.metadata.get("chunk_overlap"), k, MAX_DISTANCE, n,
                    f"{hits / n:.2f}", all_found, usable, f"{mrr:.2f}",
                    f"{refused}/{len(unanswerable)}", superseded, detail.name])
    shown = [str(x.relative_to(RAG_SYS)) if x.is_relative_to(RAG_SYS) else str(x)
             for x in (summary, detail)]
    print(f"\nLogged: {shown[0]} and {shown[1]}")
    return 1 if superseded else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--label", required=True, help="short name of this run, e.g. baseline")
    ap.add_argument("--k", type=int, default=K, help=f"chunks retrieved (default {K})")
    a = ap.parse_args()
    sys.exit(run(a.label, a.k))
