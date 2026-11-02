---
subject_scopes:
- scope-topology
version: 14
updated_at: 2026-10-29 07:45:26 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
  - CA-R-001
author: Anatoly Maslennikov
content_role: Requirement
current_scope_unit: caprmedio
status: Archived
atom_id: CA-R-040@14
type: Rule
tier: 2
subjects:
  governs: Subject/CAPRMEDIO/Graph/Rule
  depends_on: []
---
## Summary
Permit only forward Layer dependencies

## Claim

**every** dependency between Project Layers **must** point from the Project root **or** an earlier Layer **to** a later Layer **in** the cumulative order.
