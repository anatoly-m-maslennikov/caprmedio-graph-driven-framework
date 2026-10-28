---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  depends_on: []
version: 19
updated_at: 2026-10-27 19:59:29 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CA-R-1137
atom_id: CA-E-136
status: Active
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 2
---
# Reject stale Projection

## Test case

**Fixture:** change a Projection source **after** its recorded `source_frontier` **without** rebuilding the Projection.

**Expected result:** fail with the stable stale-Projection diagnostic **and** a non-zero exit.
