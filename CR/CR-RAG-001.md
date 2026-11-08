# CR-RAG-001 Chunker: step number only within its own block

| Field | Entry |
|---|---|
| Raised | 08-Nov-2026, Dr. Ebbie |
| Trigger | Deviation D3, VAL-RAG-001 §6 |
| System / version | SOP assistant MVP, code c17f360, corpus 8950971 |

## Description
A chunk after a step table inherits the table's last step number
(TM-105 v2.0 §7.2: chunks 046–048 tagged 7.2.8). answer.py passes it to the model,
which cited step 7.2.8 for the manual integration table (G07).

## Change
rag/chunker.py, _steps(): carry the previous step only if no blank line lies between
it and the chunk start. New self-test check for the manual integration table.
Change control per VAL-RAG-001 §7 (a change needs a new evaluation run); QMS-005 not yet drafted.

## Impact assessment
- Chunk texts and embeddings: unchanged (391 chunks, identical text)
- Metadata: steps changes in 6 chunks (TM-105 v2.0 046–048, v1.0 037–039)
- Retrieval: no change expected; citations: G07 no longer cites 7.2.8
- Risk: low; affects citation detail only, not which content is retrieved

## Verification (acceptance criteria, approved before the run)
1. Chunker self-test passes, including the new D3 check
2. Store rebuilt; retrieval run: hit rate and MRR unchanged (7/8, 0.69)
3. Answer run: G07 passes without citing step 7.2.8; all other results unchanged or better;
   0 superseded content, 0 invalid citations

## Approval before implementation
Reviewed: Mira Armstrong (Technical Reviewer) · 08-Nov-2026
Approved: Tess Lindqvist (QA) · 08-Nov-2026

## Closure (after implementation)
Commit: … · Runs: … · Result: … · D3 closed in VAL-RAG-001 v1.1 · date