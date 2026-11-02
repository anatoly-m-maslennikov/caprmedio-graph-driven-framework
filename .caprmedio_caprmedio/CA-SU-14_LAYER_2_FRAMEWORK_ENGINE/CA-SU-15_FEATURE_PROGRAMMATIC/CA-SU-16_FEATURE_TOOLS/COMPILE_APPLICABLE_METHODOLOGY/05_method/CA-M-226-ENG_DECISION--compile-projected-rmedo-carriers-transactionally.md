---
cce_version: cce_1
cce_form: method
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Output Publication
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Selection//Methodology Sources
  - Subject/CAPRMEDIO/Carrier
version: 23
updated_at: 2026-10-27 19:59:40 +0400
relations:
  method_for:
  - CA-R-1842
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-M-226
status: Active
content_role: Method
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eng Decision
tier: 4
---
# Compile Projected RMEDO Carriers Transactionally

**to** compile Applicable Methodology, `COMPILE_APPLICABLE_METHODOLOGY` **must** implement CA-M-224 mechanically, stage the complete projected RMEDO Carrier set under `.caprmedio_runtime`, preserve **and** revalidate **every** selected Source Carrier's repository-relative path, Atom ID, Revision, byte digest, and source Relation, **and** replace **only** files **in** `04_requirement`, `05_method`, `06_evaluation`, `07_delivery`, **and** `09_operations` through atomic file replacement with complete transaction rollback on failure. A deleted derived role tree must be fully regenerated from the same current resolved frontier; the transaction never edits source authority.

## Sources

- CA-R-1842 v1; CA-M-224; CA-O-157 v2.
