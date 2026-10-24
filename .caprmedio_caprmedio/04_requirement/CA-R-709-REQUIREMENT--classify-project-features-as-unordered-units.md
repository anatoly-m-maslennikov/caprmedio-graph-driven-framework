---
subject_scopes:
- scope-topology
version: 15
updated_at: 2026-10-24 04:48:21 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
  - CA-R-1775
author: Anatoly Maslennikov
content_role: Requirement
current_scope_unit: caprmedio
status: Active
atom_id: CA-R-709
type: Definition
tier: 0
subjects:
  governs: Subject/Domain/Node/Continuant/Scope Unit
  depends_on: []
---
# Classify Project Features as unordered units

**every** CAPRMEDIO Feature is an `unordered_unit`, is owned by **=1** immediate Structural unit, **and** has no `local_order`. a Feature owned directly by CAPRMEDIO is at Structural level `1`; a Layer-owned Feature is at Structural level `2`.
