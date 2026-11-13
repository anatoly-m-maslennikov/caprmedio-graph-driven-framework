---
atom_id: CA-R-997
ref_id: CA-R-997
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan).Header.Context.Plan.Work
    Sequence Number
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan).Header.Context.Plan.Work
    Sequence Number
tier: 3
relations:
  child_of:
  - CA-R-2712
  - CA-R-992
status: active
version: 35
updated_at: '2026-11-13T04:25:28.411819+00:00'
carrier_destination:
  file:
    name: CA-R-997-CORE_META_MODEL-RULE--validate-work-sequence-numbers.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Validate Work Sequence Numbers

## Claim

### Prose Claim

A supplied Work Sequence Number must be a positive integer. Among Active Plans, supplied Work Sequence Numbers must be unique within the same direct Container.
