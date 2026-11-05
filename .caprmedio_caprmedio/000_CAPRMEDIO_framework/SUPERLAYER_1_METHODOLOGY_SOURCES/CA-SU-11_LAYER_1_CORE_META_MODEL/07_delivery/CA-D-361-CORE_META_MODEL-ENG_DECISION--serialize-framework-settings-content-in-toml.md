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
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Data Handling <+ Serialization
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
---
## Summary

Serialize Framework Settings Content in TOML

## Claim

### Prose Claim


the Framework Instance Settings TOML Carrier.


the Framework Instance Settings TOML Carrier **must** encode explicit Operator-selected instance choices through sections **and** fields specified by concrete settings-specification Atoms under its foundational content **and** authority boundaries **and** applicable shared settings specifications; it **must not** store Project initialization inputs **or** authoritative Project Structure declarations **or** derived structural values as independently editable settings.
