---
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.Work Sequence Number
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.Work Sequence Number
version: 34
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-2712
  - CA-R-992
atom_id: CA-R-997
ref_id: CA-R-997
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Requirement
form: Rule
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-R-997-CORE_META_MODEL-RULE--validate-work-sequence-numbers.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Validate Work Sequence Numbers

## Claim

### Prose Claim


supplied Work Sequence Numbers for Plans directly contained by the same Plan or sharing the same top-level Plan container.


**every** supplied Work Sequence Number **must** be a unique positive ordinal among Plans directly contained by the same Plan **or** sharing the same top-level Plan container.
