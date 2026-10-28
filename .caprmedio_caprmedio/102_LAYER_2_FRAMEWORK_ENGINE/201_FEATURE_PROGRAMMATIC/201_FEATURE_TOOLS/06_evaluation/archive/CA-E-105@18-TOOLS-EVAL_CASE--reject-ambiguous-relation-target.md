---
subjects:
  governs: Subject/Graph Relation.Target Reference
  depends_on: []
version: 18
updated_at: 2026-10-25 17:32:27 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CA-R-1137
atom_id: CA-E-105@18
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 2
---
# Reject ambiguous relation target

## Test case

**Fixture:** make one relation stem resolve **to** two carriers.

**Expected result:** fail with the stable ambiguous-relation-target diagnostic **and** a non-zero exit.
