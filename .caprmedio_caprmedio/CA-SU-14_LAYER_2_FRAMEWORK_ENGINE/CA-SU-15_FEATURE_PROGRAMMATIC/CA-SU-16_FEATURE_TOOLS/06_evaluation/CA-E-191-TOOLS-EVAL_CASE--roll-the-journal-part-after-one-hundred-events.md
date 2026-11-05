---
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
version: 20
updated_at: 2026-11-02 19:44:26 +0400
relations:
  evaluation_for:
  - CA-R-1126
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-191
ref_id: CA-E-191
status: Active
role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
form: Eval Case
tier: 2
container:
  scope_unit: CA-SU-16
---
# Roll the Journal part after one hundred events

## Claim checked

**every** author-date Journal segment **contains** **<=100** accepted events.

## Test case

prepare `<author>-2026-08-20-part-1.ndjson` with 99 valid events, append two new events for the same author **and** date, **and** inspect both receipts **and** carriers.

## Acceptance criteria

the first append becomes line 100 of `part-1`; the second append becomes line 1 of `part-2`; neither segment **contains** more than 100 events; **and** no part number is skipped.

## Failure disposition

reject the Journal Tool **if** it overfills `part-1`, opens `part-2` early, skips a part number, **or** rewrites an admitted record.
