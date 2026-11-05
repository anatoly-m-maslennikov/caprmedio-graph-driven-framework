---
atom_id: CA-D-407
ref_id: CA-D-407
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Governing Objects/Governing Configuration
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Governing Objects/Governing Configuration
  - CAPRMEDIO_MODEL <+ Carrier/File
  - CAPRMEDIO_MODEL <+ Scope Unit
tier: 3
relations:
  child_of:
  - CA-R-1441
status: Active
version: 25
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-D-407-CORE_META_MODEL-DECISION--store-default-settings-with-the-core-meta-model-source.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Store Default Settings with the Core Meta-Model source

## Claim

### Prose Claim


the authoritative TOML File Carrier of the Default Settings Artifact.


the Default Settings Artifact **must** use `caprmedio_framework_default_settings.toml` **at** the root of the CORE_META_MODEL source Scope Unit as its **`=1`** authoritative TOML File Carrier.
