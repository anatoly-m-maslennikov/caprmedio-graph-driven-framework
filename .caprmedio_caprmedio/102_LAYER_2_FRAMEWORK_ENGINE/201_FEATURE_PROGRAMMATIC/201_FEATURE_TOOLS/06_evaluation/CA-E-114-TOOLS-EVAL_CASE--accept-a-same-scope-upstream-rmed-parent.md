---
subjects:
  governs: 'Subject/Graph Relation/Type: child_of'
  depends_on: []
version: 17
updated_at: 2026-10-25 17:32:27 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CA-R-1137
atom_id: CA-E-114
status: Active
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 2
---
# Accept a same-scope upstream RMED parent

## Test case

**Fixture:** **in** one structural scope, point a tier-classified RMED child at a parent with a lower global tier number.

**Expected result:** pass the tier-direction check.
