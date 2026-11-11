---
atom_id: CA-R-040
ref_id: CA-R-040@18
container:
  scope_unit: CA-SU-00
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit
tier: 2
relations:
  child_of:
  - CA-M-540
status: archived
version: 18
updated_at: 2026-11-11 16:42:09 +0400
carrier_destination:
  file:
    name: CA-R-040@18-RULE--permit-only-forward-layer-dependencies.md
    path: .caprmedio_caprmedio/04_requirement/archive
subject_scopes:
- scope-topology
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: caprmedio
---
## Summary
Permit only forward Layer dependencies

## Claim

### Prose Claim


**every** dependency between Project Layers **must** point from the Project root **or** an earlier Layer **to** a later Layer **in** the cumulative order.
