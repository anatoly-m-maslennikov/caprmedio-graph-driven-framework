---
atom_id: CA-R-1661
ref_id: CA-R-1661
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit.Path
  dependencies:
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit.Parent
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit.Children
tier: 3
relations:
  child_of:
  - CA-R-2530
status: Active
version: 32
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-R-1661-CORE_META_MODEL-RULE--derive-structural-path.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1661-CORE_META_MODEL-RULE--derive-structural-path.md
  source_atom_id: CA-R-1661
  source_atom_revision: 32
  source_sha256: fe9d5efe2ea6bb0ce0dce24719dd6a7e83285aa73e36ab9d3b806bcd5545d760
  original_relations_sha256: b80b8690e341472cb3c8e1b70b2e034658959f7663c4e99b6a5d6cd252ce1f53
---
## Summary

Derive Structural Path

## Claim

### Prose Claim


Structural Paths derived from active Scope Unit identities and their declared Structural Parent Relations.


**every** Structural Path **must** be derived from active Scope Unit identities **and** their declared Structural Parent Relations.

a retained representation for readability **must** remain derived **and** consistent with those authoritative inputs under CA-R-1485. it **must not** independently establish **or** change structural ancestry. permitted storage follows the applicable Delivery authority; this rule does **not** admit another authored Project Structure field.
