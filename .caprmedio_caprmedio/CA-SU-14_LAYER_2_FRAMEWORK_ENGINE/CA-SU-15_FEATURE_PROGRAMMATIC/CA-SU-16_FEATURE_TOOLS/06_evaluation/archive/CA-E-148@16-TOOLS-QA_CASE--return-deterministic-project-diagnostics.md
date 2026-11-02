---
subjects:
  governs: artifact-validation
  depends_on:
  - Subject/Graph/Relation
  - Subject/Engineering/Carrier
version: 16
updated_at: 2026-10-24 02:14:24 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CA-R-1137
atom_id: CA-E-148@16
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 2
---
# Return deterministic project diagnostics

## Test case

**Fixture:** run the missing-relation-target fixture defined by CA-E-104 twice with the same settings **and** source frontier.

**Expected result:** return identical ordered diagnostics **and** exit status on both runs.
