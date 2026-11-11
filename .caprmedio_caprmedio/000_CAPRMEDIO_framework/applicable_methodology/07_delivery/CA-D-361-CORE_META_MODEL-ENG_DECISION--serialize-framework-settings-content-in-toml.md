---
atom_id: CA-D-361
ref_id: CA-D-361
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  dependencies:
  - "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Serialization"
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Governing Objects/Governing Configuration
tier: 5
relations:
  child_of:
  - CA-D-359
status: Active
version: 32
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-D-361-CORE_META_MODEL-DECISION--serialize-framework-settings-content-in-toml.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-361-CORE_META_MODEL-ENG_DECISION--serialize-framework-settings-content-in-toml.md
  source_atom_id: CA-D-361
  source_atom_revision: 32
  source_sha256: cca5293d2d4818ccb4d25bbb3eadf6d0c0e3fc98b2033e603a2fbda69eb2b5de
  original_relations_sha256: c8bb85fb8ef619e2f610eea8ab82f269c447e9ea5167b4426122d66f74bb9054
---
## Summary

Serialize Framework Settings Content in TOML

## Claim

### Prose Claim


the Framework Instance Settings TOML Carrier.


the Framework Instance Settings TOML Carrier **must** encode explicit Operator-selected instance choices through sections **and** fields specified by concrete settings-specification Atoms under its foundational content **and** authority boundaries **and** applicable shared settings specifications; it **must not** store Project initialization inputs **or** authoritative Project Structure declarations **or** derived structural values as independently editable settings.
