# SOP RAG assistant (MVP)

**A retrieval-augmented assistant that answers questions from controlled SOPs, quotes only Effective versions and cites SOP, version and section for every statement.**

Flying Peptides training case by Dr. Ebbie. Positive Climb Diagnostics is a fictitious manufacturer; names and roles are illustrative. Not a real company, product or QMS.

Status: MVP validated (VAL-RAG-001, ISO 13485 §4.1.6) and **released for beta-testing** on 01-Nov-2026 as a training and orientation aid.

Showcase page: [flying.moichel.ch/sop-assistant](https://flying.moichel.ch/sop-assistant/)

## Why it matters

In a GxP laboratory the risk of a generic chatbot is not that it knows too little, but that it quotes the wrong version of a procedure. This project follows one method from the published paper to a governed AI tool:

1. **Paper to controlled procedure.** The methods section of a published immuno-MRM assay paper (CC BY 4.0) was rewritten as controlled method SOPs, under ISO 13485 QMS SOPs for document control and nonconforming product.
2. **Controlled procedure to machine-readable corpus.** Each SOP carries its metadata (ID, version, status, dates) as YAML front matter; every approved version is a dated, tagged Git commit.
3. **Corpus to governed AI.** Retrieval returns only Effective SOP sections, the model answers only from them, every citation is checked, and anything not covered is refused.

The corpus deliberately keeps a **Superseded** version (TM-105 v1.0, Skyline 3.6) next to the Effective one (TM-105 v2.0, Skyline 26.1). Without the status filter, the closest match to "Which Skyline version do we use?" is the superseded SOP.

## Results

Gold question set of 10 questions, approved and committed before the first test run (single-SOP, cross-document, superseded trap, near-domain unanswerable).

| Measure | Result |
|---|---|
| Gold questions passed | 8 of 10 |
| Answers with superseded content | 0 |
| Invalid citations | 0 |
| Unanswerable questions refused | 2 of 2 |
| Retrieval hit rate (k = 8) | 7 of 8, mean reciprocal rank 0.69 |

Both failures are safe refusals caused by retrieval misses: the assistant answered "Not covered by the effective SOPs." instead of guessing. Every superseded-trap and unanswerable answer was reviewed by hand. Details, risks, deviations and conditions of use: VAL-RAG-001.

## How an answer is made

1. **Retrieve** the 8 closest chunks (local embedding model all-MiniLM-L6-v2, ChromaDB, cosine distance).
2. **Filter** to status Effective and procedure content; revision history and approval rows are left out.
3. **Gate:** chunks with a distance above 0.75 are dropped; if none is left, the reply is "Not covered by the effective SOPs." and the model is not called.
4. **Answer** with Claude (claude-sonnet-5-5) only from the excerpts, citing every statement as `[TM-105 v2.0 §5.2]`.
5. **Check** every citation against the excerpts supplied; a citation that matches none, or a cut-off reply, is flagged.

Chunks are split on SOP section headings first, then by size (512 characters, 51 overlap): 391 chunks, none crossing a section.

## Corpus

| SOP | Version | Status | Approved | Effective |
|---|---|---|---|---|
| QMS-001 Document control | 1.0 | Effective | 2026-10-12 | 2026-10-26 |
| QMS-003 Control of nonconforming product | 1.0 | Effective | 2026-10-12 | 2026-10-26 |
| TM-104 Microflow MRM LC-MS acquisition | 1.0 | Effective | 2022-01-20 | 2022-02-03 |
| TM-105 Skyline data analysis | 1.0 | Superseded | 2021-05-18 | 2021-06-01 |
| TM-105 Skyline data analysis | 2.0 | Effective | 2026-10-16 | 2026-10-30 |

## Repository

| Path | Content |
|---|---|
| `SOPs/clean/` | The 5 SOPs as Markdown with YAML front matter; `master_document_list.csv` |
| `build_master_list.py` | Builds and checks the master document list from the front matter |
| `check_attribution.py` | Checks the CC BY attribution line in every method SOP, and its absence in QMS SOPs |
| `rag/` | Pipeline: `loader.py`, `chunker.py`, `store.py`, `answer.py`, `check_env.py` (each with a self-test) |
| `eval/gold_questions.csv` | The approved gold question set |
| `eval/hit_rate.py`, `eval/answer_eval.py` | Retrieval and answer evaluation; every run is logged in `eval/runs/` |

Git history: one commit per approved SOP version, dated to its approval date and tagged (e.g. `TM-105_v2.0`); code and evaluation commits carry their real date. The validated code is commit `c17f360`, the corpus commit `8950971`, the gold set commit `8fd6ce0`.

## Run it

Python 3.11, Windows PowerShell, from this folder:

```powershell
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Set the Anthropic API key as a user environment variable named `ANTHROPIC_API_KEY` (never in a file), restart the terminal, then:

```powershell
python rag\check_env.py                          # environment check
python rag\store.py                              # build the store and run its self-test
python rag\answer.py "Which Skyline version do we use?"
python eval\hit_rate.py --label my-run           # retrieval evaluation, no API cost
python eval\answer_eval.py --label my-run        # answer evaluation, about 10 API calls
```

Rebuild the store after every SOP change, and repeat both evaluation runs before further use.

## Conditions of use

- Training and orientation aid only; never for release, disposition or acceptance decisions.
- Open the cited section of the Effective SOP before acting: the SOP, not the answer, is the authority.
- "Not covered by the effective SOPs." means "check the SOP index", not "no requirement exists".

## Next (full build)

Follow cross-references between SOPs, add keyword search, a gold set of 20+ questions with acceptance criteria approved before any run, risk assessment and traceability, a simple local question interface, and the remaining SOPs (TM-101 to TM-103, TM-106, QMS-002, QMS-004 to QMS-006).

## License

Code: MIT. SOPs, gold questions, evaluation data and this README: CC BY 4.0. The method SOPs keep the attribution below. See [LICENSE](LICENSE) for details, including what is not licensed (patent, trade mark).

## Attribution

Method SOPs adapted from: Bringans S, Ito J, Casey T, et al. "A robust multiplex immunoaffinity mass spectrometry assay (PromarkerD) for clinical prediction of diabetic kidney disease." *Clin Proteomics* 2020;17:37. doi:10.1186/s12014-020-09302-w. Licensed under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). The methods were restructured and rewritten as controlled procedures for a fictitious company; procedural detail was added for training purposes. The authors, Proteomics International and Atturos do not endorse this work.

CC BY 4.0 covers the paper's text only, not the biomarker patent or the PromarkerD trade mark; the corpus uses neutral names ("3-plex immuno-MRM DKD assay").

*Flying Peptides: where proteins take flight. Making the proteomics world unshady.*
