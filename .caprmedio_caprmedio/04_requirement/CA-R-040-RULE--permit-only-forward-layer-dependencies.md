---
atom_id: CA-R-040
ref_id: CA-R-040
container:
  scope_unit: CA-SU-00
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit
tier: 2
relations:
  child_of:
  - CA-R-2691
status: Active
version: 17
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-R-040-CAPRMEDIO-RULE--permit-only-forward-layer-dependencies.md
    path: .caprmedio_caprmedio/04_requirement
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
