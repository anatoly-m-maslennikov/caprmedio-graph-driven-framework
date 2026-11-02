---
subjects:
  governs: Subject/Graph Node/Engineering/Continuant/Carrier
  depends_on:
  - Subject/Graph Node/Engineering/Continuant/Carrier
version: 20
updated_at: 2026-10-25 17:32:27 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CA-R-1136
atom_id: CA-E-099@20
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 2
---
# Preserve carrier bytes after validation failure

## Test case

**Fixture:** run the malformed-filename fixture defined by CA-E-073 **and** compare the complete carrier bytes **before** **and** **after** validation.

**Expected result:** return the malformed-filename failure while preserving byte-identical carrier content.
