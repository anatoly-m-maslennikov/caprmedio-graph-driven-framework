---
atom_id: CA-R-997
ref_id: CA-R-997
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.Work Sequence Number
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.Work Sequence Number
tier: 3
relations:
  child_of:
  - CA-R-2712
  - CA-R-992
status: Active
version: 34
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-997-CORE_META_MODEL-RULE--validate-work-sequence-numbers.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-997-CORE_META_MODEL-RULE--validate-work-sequence-numbers.md
  source_atom_id: CA-R-997
  source_atom_revision: 34
  source_sha256: 9bc15e2b13707d6ec0f6a507071f8364ff9447a6036262158f529d7adc3f07c7
  original_relations_sha256: 67780ad08f4f9ebb0b72dc35b08b9596c5a490e92d8b08ccb2c9878b326f6d40
---
## Summary

Validate Work Sequence Numbers

## Claim

### Prose Claim


supplied Work Sequence Numbers for Plans directly contained by the same Plan or sharing the same top-level Plan container.


**every** supplied Work Sequence Number **must** be a unique positive ordinal among Plans directly contained by the same Plan **or** sharing the same top-level Plan container.
