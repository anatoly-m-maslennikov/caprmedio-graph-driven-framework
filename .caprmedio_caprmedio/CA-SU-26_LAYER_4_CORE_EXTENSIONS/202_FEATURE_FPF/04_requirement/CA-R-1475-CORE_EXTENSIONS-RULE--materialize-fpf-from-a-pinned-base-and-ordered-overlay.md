---
atom_id: CA-R-1475
ref_id: CA-R-1475
container:
  scope_unit: CA-SU-26
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Source Selection
  dependencies:
  - Subject/caprmedio/Extension//FPF
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Traceability
tier: 1
status: Active
version: 17
updated_at: 2026-10-27 19:59:55 +0400
cce_version: cce_1
cce_form: obligation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: CORE_EXTENSIONS
author: Anatoly Maslennikov
---
# Materialize FPF from a pinned base and ordered overlay

**every** FPF Extension Candidate **must** be materialized reproducibly from **`=1`** exact upstream FPF source revision **and** **`=1`** ordered project-owned patch overlay, **and** its immutable manifest **must** identify the complete base inventory **and** digest, **every** ordered overlay input **and** digest, the resulting inventory **and** digest, the exact Extension version, the intended behavior changes, preserved upstream behavior, affected paths, **and** acceptance Evaluations.
