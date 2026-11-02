---
subjects:
  governs: artifact-validation
  depends_on:
  - Subject/Graph/Relation
  - Subject/Engineering/Carrier
version: 15
updated_at: 2026-10-24 01:18:03 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CA-R-1137
atom_id: CA-E-147@15
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
---
# Preserve project bytes after validation failure

## Test case

**Fixture:** run the missing-relation-target fixture defined by CA-E-104 **and** compare **all** project bytes **before** **and** **after** validation.

**Expected result:** return the missing-relation-target failure while preserving byte-identical project content.
