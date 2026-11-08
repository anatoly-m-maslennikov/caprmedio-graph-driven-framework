---
atom_id: CA-D-359
ref_id: CA-D-359
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings
  dependencies:
  - CAPRMEDIO_MODEL <+ Carrier/File
tier: 4
relations:
  child_of:
  - CA-D-358
status: Active
version: 30
updated_at: 2026-11-04 09:30:21 +0400
carrier_destination:
  file:
    name: CA-D-359-CORE_META_MODEL-DECISION--bind-framework-settings-to-its-authoritative-toml-carrier.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-359-CORE_META_MODEL-ENG_DECISION--bind-framework-settings-to-its-authoritative-toml-carrier.md
  source_atom_id: CA-D-359
  source_atom_revision: 30
  source_sha256: d7a0ffea1735dc4f2159cc8b7321e8f22e9b37b950a03e745b1f5a2230a8efbc
  original_relations_sha256: 548de335dd35782717651df33fa6bc32b2fe029d2515df86f0a3bb59ab940171
---
## Summary

Bind Framework Settings to Its Authoritative TOML Carrier

## Claim

### Prose Claim


the existing Framework Settings TOML Carrier for a Project named `<project_name>`.


the Framework Settings Carrier for a Project named `<project_name>` **must** use `.caprmedio_<project_name>/000_CAPRMEDIO_framework/caprmedio_framework_settings.toml` as its **`=1`** authoritative TOML File Carrier for the Project.Settings fields registered to that physical partition.
