---
subject_scopes:
- scope-topology
version: 25
updated_at: 2026-10-30 03:53:02 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
author: Anatoly Maslennikov
content_role: Requirement
current_scope_unit: caprmedio
status: Archived
atom_id: CA-R-709@25
type: Rule
tier: 0
subjects:
  governs: Entity/Object/Continuant/Structural Unit/Scope Unit
  depends_on: []
claim_target_scope_unit: caprmedio
---
## Summary

Classify Project Features as unordered units

## Claim

**Every** CAPRMEDIO Feature:

- is an `unordered_unit`;
- is owned by **=1** immediate Structural unit; **and**
- has no `local_order`.
