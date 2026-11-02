---
subjects:
  governs: Subject/Domain/Node/Continuant/History/Journal.Record
  depends_on:
  - Subject/Domain/Node/Continuant/History/Journal
  - Subject/Domain/Node/Continuant/Projection
version: 17
updated_at: 2026-10-24 08:53:16 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CAPRMEDIO-GOV-REQU-367
  - CA-R-1137
atom_id: CA-E-141@17
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 2
---
# Reject duplicate terminal event

## Test case

**Fixture:** record two terminal Events for the same Work Journal Action identifying one Projection Rebuild under CAPRMEDIO-GOV-REQU-367. events belonging **to** separately identified rebuild Actions are **not** this duplicate fixture.

**Expected result:** fail the duplicate terminal Events for that Action with the stable duplicate-terminal-event diagnostic **and** a non-zero exit.
