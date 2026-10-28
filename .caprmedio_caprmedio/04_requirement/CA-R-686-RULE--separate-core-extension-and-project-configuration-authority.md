---
version: 25
updated_at: 2026-10-27 20:00:10 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
  - CA-M-001
  - CA-M-006
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit//PROJECT_CONFIGURATION
  - 'Subject/caprmedio/Product: CAPRMEDIO Framework'
cce_version: cce_1
cce_form: obligation
author: Anatoly Maslennikov
content_role: Requirement
current_scope_unit: caprmedio
status: Active
atom_id: CA-R-686
type: Rule
tier: 1
---
# Separate core, Extension, and Project Configuration authority

CAPRMEDIO **must** govern core methodology authority, reusable Extension authority, **and** Project-specific Project Configuration authority as distinct strata **without** copying **or** silently transferring meaning among them.
