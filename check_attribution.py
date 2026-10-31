"""Check the CC BY 4.0 attribution line in the SOP corpus.

Usage:  python check_attribution.py [corpus_folder]   (default: SOPs/clean next to this script)
Source: the attribution line is read from the Guardrails blockquote in RAG_SOP_Masterplan.html
        next to this script, so the check always uses the current approved wording.
Checks: every Method SOP contains the full line exactly once, with all four CC BY elements
        (credit, licence link, changes indicated, no endorsement), and front matter
        source = "Bringans et al. 2020, CC BY 4.0";
        no QMS SOP contains the line or any part of it, and front matter source = null.
Exit code 1 if a check fails.
Flying Peptides training case. Fictitious manufacturer: Positive Climb Diagnostics.
"""
import html, re, sys
from pathlib import Path
import yaml

HERE = Path(__file__).parent
SOURCE = "Bringans et al. 2020, CC BY 4.0"
# Fragment that identifies each CC BY 4.0 element inside the full line.
ELEMENTS = {
    "credit": "Bringans S, Ito J, Casey T, et al.",
    "licence link": "https://creativecommons.org/licenses/by/4.0/",
    "changes indicated": "restructured and rewritten as controlled procedures",
    "no endorsement": "do not endorse this document",
}
# Any of these in a QMS SOP means attribution text leaked in.
QMS_FORBIDDEN = ["Adapted from:", "Bringans", "creativecommons.org", "CC BY", "do not endorse"]


def norm(text):
    return re.sub(r"\s+", " ", text).strip()


def guardrail_line():
    page = (HERE / "RAG_SOP_Masterplan.html").read_text(encoding="utf-8")
    quotes = [q for q in re.findall(r"<blockquote[^>]*>(.*?)</blockquote>", page, re.S)
              if "Adapted from:" in q]
    if len(quotes) != 1:
        sys.exit(f"Masterplan: expected 1 attribution blockquote, found {len(quotes)}")
    return norm(html.unescape(re.sub(r"<[^>]+>", "", quotes[0])))


def md_body_text(text):
    """Markdown to comparable plain text: links to their URL, emphasis markers removed."""
    text = re.sub(r"\[([^\]]*)\]\(([^)]*)\)", r"\2", text)
    text = re.sub(r"(?<![\\*])\*{1,2}(?!\*)", "", text)
    return norm(text)


def main():
    folder = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "SOPs" / "clean"
    line = guardrail_line()
    for name, frag in ELEMENTS.items():
        if frag not in line:
            sys.exit(f"Masterplan line lacks the {name} element ('{frag}')")
    problems, n_tm, n_qms = [], 0, 0
    for path in sorted(folder.glob("*.md")):
        raw = path.read_text(encoding="utf-8")
        fm = yaml.safe_load(raw.split("---\n", 2)[1])
        body = md_body_text(raw.split("---\n", 2)[2])
        doc_type, prefix = fm.get("doc_type"), path.name.split("-")[0]
        if doc_type == "Method SOP":
            n_tm += 1
            if prefix != "TM":
                problems.append(f"{path.name}: doc_type Method SOP but file name is not TM-")
            count = body.count(line)
            if count != 1:
                problems.append(f"{path.name}: full attribution line found {count} times (expected 1)")
            for name, frag in ELEMENTS.items():
                if frag not in body:
                    problems.append(f"{path.name}: missing {name} element")
            if fm.get("source") != SOURCE:
                problems.append(f"{path.name}: front matter source is {fm.get('source')!r}")
        elif doc_type == "QMS SOP":
            n_qms += 1
            if prefix != "QMS":
                problems.append(f"{path.name}: doc_type QMS SOP but file name is not QMS-")
            for frag in QMS_FORBIDDEN:
                if frag in body:
                    problems.append(f"{path.name}: QMS SOP contains attribution text '{frag}'")
            if fm.get("source") is not None:
                problems.append(f"{path.name}: front matter source should be null")
        else:
            problems.append(f"{path.name}: unknown doc_type {doc_type!r}")
        print(f"{'FAIL' if any(p.startswith(path.name) for p in problems) else 'ok  '}  {path.name}")
    print(f"{n_tm} method SOPs, {n_qms} QMS SOPs checked.")
    if problems:
        print("\n".join(problems))
        sys.exit(1)
    print("All attribution checks passed.")


if __name__ == "__main__":
    main()
