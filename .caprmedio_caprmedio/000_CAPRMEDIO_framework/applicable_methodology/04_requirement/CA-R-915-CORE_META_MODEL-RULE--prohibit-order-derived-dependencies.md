---
atom_id: CA-R-915
ref_id: CA-R-915
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation
tier: 2
relations:
  child_of:
  - CA-R-913@24
status: Active
version: 33
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-R-915-CORE_META_MODEL-RULE--prohibit-order-derived-dependencies.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-915-CORE_META_MODEL-RULE--prohibit-order-derived-dependencies.md
  source_atom_id: CA-R-915
  source_atom_revision: 33
  source_sha256: 2760c1673d2ad6728f608204975d7460d7eefd1c7a8e2480cec154dee87f4324
  original_relations_sha256: 37bddd092dba1e824684b18eaeff64ca705f32a1fc76143ef62013a5fb7fafc8
---
## Summary
Prohibit order-derived dependencies

## Claim

### Prose Claim


Dependencies between related Governed Entities.


the Local Order of two Scope Units **or** the position of one canonical target reference **in** `relations.<RELATION_KIND>` **must not** establish **or** alter a dependency between related Governed Entities.
