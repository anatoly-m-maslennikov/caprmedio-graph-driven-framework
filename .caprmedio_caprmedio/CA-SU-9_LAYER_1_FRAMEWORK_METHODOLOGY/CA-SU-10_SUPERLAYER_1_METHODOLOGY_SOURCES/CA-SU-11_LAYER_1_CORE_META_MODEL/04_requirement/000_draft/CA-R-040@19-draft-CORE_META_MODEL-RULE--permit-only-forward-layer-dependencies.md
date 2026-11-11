---
atom_id: CA-R-040
ref_id: CA-R-040@19-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit
tier: 2
relations:
  child_of:
  - CA-M-540
status: Draft
version: 19
updated_at: 2026-11-11 17:36:24 +0400
carrier_destination:
  file:
    name: CA-R-040@19-draft-CORE_META_MODEL-RULE--permit-only-forward-layer-dependencies.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft
subject_scopes:
- scope-topology
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: CORE_META_MODEL
---
## Summary
Permit only forward Layer dependencies

## Claim

### Prose Claim


**every** dependency between Project Layers **must** point from the Project root **or** an earlier Layer **to** a later Layer **in** the cumulative order.
