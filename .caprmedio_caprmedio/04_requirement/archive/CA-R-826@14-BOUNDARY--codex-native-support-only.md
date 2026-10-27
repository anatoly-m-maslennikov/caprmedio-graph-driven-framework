---
subject_scopes:
- applicability
version: 14
updated_at: 2026-10-25 17:32:27 +0400
relations: {}
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-826@14
status: Archived
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: caprmedio
type: Boundary
tier: 2
subjects:
  governs: Subject/Graph Node/Engineering/Codex Plugin
  depends_on: []
---
# Codex native support only

CAPRMEDIO's current native LLM-application support set **contains** Codex **and** no other application. Native support **means** that CAPRMEDIO owns **and** maintains the application adapter required **to** install **and** invoke framework interfaces **and** resolve host-session identity **without** an Extension **or** operator-provided compatibility layer. **every** other LLM application remains outside native support **until** an applicable active Boundary Requirement expands **or** replaces this Boundary.
