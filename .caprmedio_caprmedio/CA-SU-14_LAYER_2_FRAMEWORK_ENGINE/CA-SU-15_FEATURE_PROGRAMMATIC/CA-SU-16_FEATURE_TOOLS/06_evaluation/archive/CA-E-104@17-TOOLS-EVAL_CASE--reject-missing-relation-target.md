---
subjects:
  governs: Subject/Graph/Relation.Target Reference
  depends_on: []
version: 17
updated_at: 2026-10-24 11:58:20 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CA-R-1137
atom_id: CA-E-104@17
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 2
---
# Reject missing relation target

## Test case

**Fixture:** point one relation at a nonexistent canonical filename stem.

**Expected result:** fail with the stable missing-relation-target diagnostic **and** a non-zero exit.
