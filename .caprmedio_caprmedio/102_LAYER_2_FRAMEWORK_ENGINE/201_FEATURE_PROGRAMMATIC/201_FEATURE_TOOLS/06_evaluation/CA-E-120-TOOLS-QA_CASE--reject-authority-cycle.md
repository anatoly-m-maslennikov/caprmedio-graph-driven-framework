---
subjects:
  governs: artifact-validation
  depends_on: []
version: 20
updated_at: 2026-10-24 02:14:24 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CA-R-1137
  - CA-R-833
  - CA-E-481
  - CA-R-030
atom_id: CA-E-120
status: Active
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 2
---
# Reject authority cycle

## Test case

**Fixture:** add one `child_of` edge that closes a cycle.

**Expected result:** fail with the stable authority-cycle diagnostic **and** a non-zero exit.
