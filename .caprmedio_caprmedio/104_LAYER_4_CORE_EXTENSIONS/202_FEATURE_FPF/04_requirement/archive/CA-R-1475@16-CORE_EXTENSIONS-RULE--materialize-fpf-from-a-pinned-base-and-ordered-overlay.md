---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: Subject/Graph Node/Engineering/Data Handling/Source Selection
  depends_on:
  - Subject/Graph Node/Product/Extension//FPF
  - Subject/Graph Node/Engineering/Traceability
version: 16
updated_at: 2026-10-27 06:04:45 +0400
relations: {}
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
content_role: Requirement
current_scope_unit: CORE_EXTENSIONS
status: Archived
author: Anatoly Maslennikov
atom_id: CA-R-1475@16
type: Rule
tier: 1
---
# Materialize FPF from a pinned base and ordered overlay

**every** FPF Extension Candidate **must** be materialized reproducibly from **`=1`** exact upstream FPF source revision **and** **`=1`** ordered project-owned patch overlay, **and** its immutable manifest **must** identify the complete base inventory **and** digest, **every** ordered overlay input **and** digest, the resulting inventory **and** digest, the exact Extension version, the intended behavior changes, preserved upstream behavior, affected paths, **and** acceptance Evaluations.
