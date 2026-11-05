---
atom_id: CA-E-099
ref_id: CA-E-099
container:
  scope_unit: CA-SU-16
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Storage
  dependencies:
  - Subject/CAPRMEDIO/Carrier
tier: 2
relations:
  evaluation_for:
  - CA-R-1136
status: Active
version: 23
updated_at: 2026-10-27 19:59:28 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Preserve carrier bytes after validation failure

## Test case

**Fixture:** run the malformed-filename fixture defined by CA-E-073 **and** compare the complete carrier bytes **before** **and** **after** validation.

**Expected result:** return the malformed-filename failure while preserving byte-identical carrier content.
