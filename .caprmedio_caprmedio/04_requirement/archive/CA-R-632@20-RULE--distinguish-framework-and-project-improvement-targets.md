---
version: 20
updated_at: 2026-10-25 02:38:20 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
  - CA-R-1423
subjects:
  governs: Subject/Domain/Node/Continuant/Project
  depends_on:
  - Subject/Domain/Node/Continuant/Project
  - Subject/Engineering/Framework Instance
  - 'Subject/Product: CAPRMEDIO Framework'
cce_version: cce_1
cce_form: obligation
author: Anatoly Maslennikov
content_role: Requirement
current_scope_unit: caprmedio
status: Archived
atom_id: CA-R-632@20
type: Rule
tier: 1
---
# Distinguish framework and Project improvement targets

**every** governed improvement cycle **in** caprmedio **must** declare **`=1`** primary target:

- the CAPRMEDIO Framework Instance operating within caprmedio; **or**
- the CAPRMEDIO Framework being developed as the caprmedio Project's output.
