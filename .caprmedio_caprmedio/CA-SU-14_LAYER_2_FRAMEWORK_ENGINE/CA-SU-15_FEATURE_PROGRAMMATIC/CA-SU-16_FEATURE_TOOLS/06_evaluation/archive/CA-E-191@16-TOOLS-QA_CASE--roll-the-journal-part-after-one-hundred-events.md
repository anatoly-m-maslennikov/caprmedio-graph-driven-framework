---
subjects:
  governs: Work Journal/Segment
  depends_on: []
version: 16
updated_at: 2026-10-24 02:14:24 +0400
relations:
  evaluation_for:
  - CA-R-1126
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-191@16
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 2
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
