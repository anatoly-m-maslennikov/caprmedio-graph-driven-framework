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
---
## Summary

Bind Framework Settings to Its Authoritative TOML Carrier

## Claim

### Prose Claim


the existing Framework Settings TOML Carrier for a Project named `<project_name>`.


the Framework Settings Carrier for a Project named `<project_name>` **must** use `.caprmedio_<project_name>/000_CAPRMEDIO_framework/caprmedio_framework_settings.toml` as its **`=1`** authoritative TOML File Carrier for the Project.Settings fields registered to that physical partition.
