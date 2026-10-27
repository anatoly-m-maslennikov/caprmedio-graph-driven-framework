---
subjects:
  governs: Subject/Graph Relation/Type
  depends_on: []
version: 18
updated_at: 2026-10-25 17:32:27 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CA-R-1137
atom_id: CA-E-109
status: Active
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 2
---
# Reject relation target Type

## Test case

**Fixture:** use a registered relation kind toward a target Type it does **not** admit.

**Expected result:** fail with the stable relation-target-Type diagnostic **and** a non-zero exit.
