---
subject_scopes:
- scope-topology
version: 19
updated_at: 2026-10-25 17:32:27 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
author: Anatoly Maslennikov
content_role: Requirement
current_scope_unit: caprmedio
status: Active
atom_id: CA-R-709
type: Definition
tier: 0
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Scope Unit
  depends_on: []
---
# Classify Project Features as unordered units

**every** CAPRMEDIO Feature is an `unordered_unit`, is owned by **=1** immediate Structural unit, **and** has no `local_order`.
