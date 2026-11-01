"""Phase 5: end-to-end answer evaluation on the gold question set.

Usage (from the RAG_sys folder, venv active; store built with python rag\store.py):
    python eval\answer_eval.py --label baseline
Calls the model once per question that passes the distance cut-off (about 10 short calls).
Each run is logged: one summary row appended to eval/runs/answer_runs.csv and one detail file
eval/runs/answer_<timestamp>_<label>.csv with the full reply of every question and two empty
columns, manual_verdict and manual_reviewer, for the manual check of the unanswerable and
superseded-trap answers (Masterplan, Answer scoring). Commit both files after the review.

Automatic checks
  answerable (single, cross, trap):
    answered       the reply is not the not-covered reply
    contains       must_contain appears in the reply
    excludes       must_not_contain does not appear in the reply
    citations ok   at least one valid citation and none that matches no excerpt (rag/answer.py)
    cites expected at least one citation points to an expected source (same doc_key, same
                   section or a step in it); "all expected" is reported for cross questions
    pass           all of the above
  unanswerable:
    refused        the reply contains "Not covered by the effective SOPs."
    strict         the reply is exactly that sentence (anything more is shown for review)
    pass           refused, and no citation that matches no excerpt
Text comparison ignores case, spaces and the difference between the micro sign and Greek mu.
Flying Peptides training case. Fictitious manufacturer: Positive Climb Diagnostics.
"""
import argparse
import csv
import datetime
import re
import sys
from pathlib import Path

EVAL = Path(__file__).resolve().parent
RAG_SYS = EVAL.parent
sys.path.insert(0, str(RAG_SYS / "rag"))
sys.path.insert(0, str(EVAL))
from answer import CITATION, MAX_DISTANCE, MODEL, NOT_COVERED, answer, call_claude  # noqa: E402
from hit_rate import git, load_gold  # noqa: E402
from store import K, get_collection  # noqa: E402

RUNS = EVAL / "runs"


def squash(text):
    return re.sub(r"\s+", "", text.replace("μ", "µ")).lower()


def cited(valid, source):
    key, section = source
    for c in valid:
        m = CITATION.match(c)
        if m and f"{m.group(1)} v{m.group(2)}" == key and (
                m.group(3) == section or m.group(3).startswith(section + ".")):
            return True
    return False


def evaluate(row, r):
    reply = r["reply"]
    out = {"id": row["id"], "type": row["type"], "question": row["question"],
           "expected": row["expected_sources"], "model_called": r["called_model"],
           "chunks_used": len(r["hits"]), "best_distance": r["best_distance"],
           "citations": "; ".join(r["valid"]), "invalid_citations": "; ".join(r["invalid"])}
    if not row["sources"]:
        refused = NOT_COVERED in reply
        out.update(answered="", contains="", excludes="", citations_ok="",
                   cites_expected="", all_expected="", refused=refused,
                   strict=reply.strip() == NOT_COVERED, passed=refused and not r["invalid"])
    else:
        must, must_not = row["must_contain"].strip(), row["must_not_contain"].strip()
        found = [cited(r["valid"], s) for s in row["sources"]]
        checks = {
            "answered": not reply.strip().startswith(NOT_COVERED),
            "contains": (squash(must) in squash(reply)) if must else True,
            "excludes": (squash(must_not) not in squash(reply)) if must_not else True,
            "citations_ok": bool(r["valid"]) and not r["invalid"],
            "cites_expected": any(found),
        }
        out.update(checks, all_expected=all(found), refused="", strict="",
                   passed=all(checks.values()))
    out.update(reply=reply, manual_verdict="", manual_reviewer="")
    return out


def run(label, llm=call_claude, collection=None, runs_dir=RUNS):
    col = collection or get_collection()
    gold = load_gold()
    model = MODEL if llm is call_claude else getattr(llm, "__name__", "test model")
    print(f"Gold set: {len(gold)} questions; model {model}; k = {K}; "
          f"MAX_DISTANCE = {MAX_DISTANCE}")
    print(f"Store: built {col.metadata.get('built_at')}, corpus commit "
          f"{col.metadata.get('corpus_commit')}\n")
    results = []
    for row in gold:
        res = evaluate(row, answer(row["question"], llm=llm, collection=col))
        results.append(res)
        yn = lambda v: "-" if v == "" else ("yes" if v else "NO")  # noqa: E731
        print(f"{res['id']} {res['type']:<12} {'PASS' if res['passed'] else 'FAIL'}  "
              f"{row['question']}")
        if row["sources"]:
            print(f"     answered {yn(res['answered'])} | contains '{row['must_contain'] or '-'}' "
                  f"{yn(res['contains'])} | excludes '{row['must_not_contain'] or '-'}' "
                  f"{yn(res['excludes'])} | citations ok {yn(res['citations_ok'])} | "
                  f"cites expected {yn(res['cites_expected'])} (all {yn(res['all_expected'])})")
        else:
            print(f"     refused {yn(res['refused'])} | strict {yn(res['strict'])} | "
                  f"model called {yn(res['model_called'])} (best distance {res['best_distance']})")
        print(f"     citations: {res['citations'] or 'none'}"
              + (f" | NOT IN EXCERPTS: {res['invalid_citations']}" if res["invalid_citations"] else ""))
        print("     " + res["reply"].replace("\n", "\n     ") + "\n")

    ans = [r for r in results if r["answered"] != ""]
    una = [r for r in results if r["answered"] == ""]
    traps = [r for r in results if r["type"] == "trap"]
    n_pass = sum(r["passed"] for r in results)
    print(f"Passed: {n_pass}/{len(results)}   answerable {sum(r['passed'] for r in ans)}/{len(ans)}"
          f"   superseded traps {sum(r['passed'] for r in traps)}/{len(traps)}"
          f"   unanswerable refused {sum(r['passed'] for r in una)}/{len(una)}")
    print(f"Expected source cited: {sum(r['cites_expected'] for r in ans)}/{len(ans)}   "
          f"all expected sources cited: {sum(r['all_expected'] for r in ans)}/{len(ans)}   "
          f"invalid citations: {sum(bool(r['invalid_citations']) for r in results)}")
    print("Manual review: fill manual_verdict and manual_reviewer in the detail file for "
          + ", ".join(r["id"] for r in results if r["type"] in ("trap", "unanswerable")) + ".")

    stamp = datetime.datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    safe = re.sub(r"[^A-Za-z0-9_-]+", "-", label).strip("-") or "run"
    runs_dir.mkdir(exist_ok=True)
    detail = runs_dir / f"answer_{stamp}_{safe}.csv"
    with open(detail, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(results[0]))
        w.writeheader()
        w.writerows(results)
    summary = runs_dir / "answer_runs.csv"
    new = not summary.exists()
    dirty = " (uncommitted changes)" if git("status", "--porcelain", "--", "rag", "SOPs/clean",
                                            "eval/gold_questions.csv", "eval/answer_eval.py") else ""
    with open(summary, "a", encoding="utf-8-sig" if new else "utf-8", newline="") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["run_at", "label", "code_commit", "corpus_commit", "store_built_at",
                        "model", "k", "max_distance", "passed", "answerable_passed",
                        "traps_passed", "unanswerable_refused", "expected_cited",
                        "all_expected_cited", "invalid_citations", "detail_file"])
        w.writerow([stamp, label, git("rev-parse", "--short", "HEAD") + dirty,
                    col.metadata.get("corpus_commit"), col.metadata.get("built_at"), model, K,
                    MAX_DISTANCE, f"{n_pass}/{len(results)}",
                    f"{sum(r['passed'] for r in ans)}/{len(ans)}",
                    f"{sum(r['passed'] for r in traps)}/{len(traps)}",
                    f"{sum(r['passed'] for r in una)}/{len(una)}",
                    f"{sum(r['cites_expected'] for r in ans)}/{len(ans)}",
                    f"{sum(r['all_expected'] for r in ans)}/{len(ans)}",
                    sum(bool(r["invalid_citations"]) for r in results), detail.name])
    shown = [str(x.relative_to(RAG_SYS)) if x.is_relative_to(RAG_SYS) else str(x)
             for x in (summary, detail)]
    print(f"\nLogged: {shown[0]} and {shown[1]}")
    return 0 if n_pass == len(results) else 1


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--label", required=True, help="short name of this run, e.g. baseline")
    sys.exit(run(ap.parse_args().label))
