---
atom_id: CA-R-954
ref_id: CA-R-954
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Demand)'
  dependencies:
  - CAPRMEDIO_MODEL <+ Package/Implementation
tier: 6
relations:
  child_of:
  - CA-R-933
status: Active
version: 33
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-954-CORE_META_MODEL-RULE--target-one-implementation-result-with-each-demand.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-954-CORE_META_MODEL-RULE--target-one-implementation-result-with-each-demand.md
  source_atom_id: CA-R-954
  source_atom_revision: 33
  source_sha256: 8a8e008e8314a3689af2841c21a9aed66f0ca889cb4d542485235b9b422ac03b
  original_relations_sha256: c28d84bac21e6f7cc7bfde47da5b055ffadede71bf17c4da3c8b2456c1f525ea
---
## Summary
Target one Implementation result with each Demand

## Claim

### Prose Claim


Demand Atoms.


**every** Demand Atom **must** constrain **`=1`** Implementation result produced by its Claim Scope.
