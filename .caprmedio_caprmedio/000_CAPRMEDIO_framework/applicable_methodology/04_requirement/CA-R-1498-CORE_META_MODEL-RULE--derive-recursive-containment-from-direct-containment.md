---
atom_id: CA-R-1498
ref_id: CA-R-1498
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity
  dependencies:
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//CONTAINS
tier: 1
status: Active
version: 17
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1498-CORE_META_MODEL-RULE--derive-recursive-containment-from-direct-containment.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1498-CORE_META_MODEL-RULE--derive-recursive-containment-from-direct-containment.md
  source_atom_id: CA-R-1498
  source_atom_revision: 17
  source_sha256: ad372d8f5959f64f92a19ac495b10066d6d5fd6bd3d3ac64edfaabc8747d7581
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Derive Recursive Containment from Direct Containment

## Claim

### Prose Claim


recursive Structural Entity containment.


recursive Structural Entity containment **must** **`=`** the transitive closure of direct Structural Entity containment.
