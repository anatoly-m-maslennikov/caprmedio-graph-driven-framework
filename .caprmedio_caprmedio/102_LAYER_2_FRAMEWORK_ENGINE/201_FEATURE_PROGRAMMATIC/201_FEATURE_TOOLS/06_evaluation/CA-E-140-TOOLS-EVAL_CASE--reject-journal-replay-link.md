---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/History/Journal.Record
  depends_on: []
version: 18
updated_at: 2026-10-25 17:32:27 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CA-R-1137
atom_id: CA-E-140
status: Active
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 2
---
# Reject Journal replay link

## Test case

**Fixture:** point one Work Journal event at a nonexistent preceding event.

**Expected result:** fail with the stable Journal-replay-link diagnostic **and** a non-zero exit.
