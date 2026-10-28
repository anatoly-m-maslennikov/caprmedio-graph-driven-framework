---
version: 22
updated_at: 2026-10-27 19:59:48 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
  - CA-E-002
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Requirement'
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Concern'
  - 'Subject/caprmedio/Product: CAPRMEDIO Framework'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
cce_version: cce_1
cce_form: obligation
author: Anatoly Maslennikov
content_role: Requirement
current_scope_unit: caprmedio
status: Active
atom_id: CA-R-024
type: Rule
tier: 2
---
# Govern Requirement conflicts by tier

CAPRMEDIO **must** resolve conflicts among active non-Principle Requirements through explicit rules determined by their applicability tiers rather than presentation order, Concern priority, **or** implicit interpretation.
