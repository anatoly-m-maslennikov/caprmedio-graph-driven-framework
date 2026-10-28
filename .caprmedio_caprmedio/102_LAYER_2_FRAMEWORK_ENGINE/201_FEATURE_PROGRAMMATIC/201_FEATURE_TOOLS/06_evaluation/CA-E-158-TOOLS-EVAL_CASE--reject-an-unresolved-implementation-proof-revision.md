---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification/Static Analysis
  depends_on: []
version: 21
updated_at: 2026-10-27 19:59:29 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CA-R-1137
atom_id: CA-E-158
status: Active
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 2
---
# Reject an unresolved implementation proof revision

## Test case

**Fixture:** leave one required implementation revision unresolved **in** a proof frontier.

**Expected result:** fail with the stable incomplete-proof-frontier diagnostic **and** a non-zero exit.
