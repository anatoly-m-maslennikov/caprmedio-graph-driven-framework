---
atom_id: CA-D-364
ref_id: CA-D-364
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings
  dependencies:
  - CAPRMEDIO_MODEL <+ Carrier/File
tier: 5
relations:
  child_of:
  - CA-D-363
status: Active
version: 30
updated_at: 2026-11-03 23:25:51 +0400
carrier_destination:
  file:
    name: CA-D-364-CORE_META_MODEL-DECISION--bind-project-settings-to-its-authoritative-toml-carrier.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-364-CORE_META_MODEL-ENG_DECISION--bind-project-settings-to-its-authoritative-toml-carrier.md
  source_atom_id: CA-D-364
  source_atom_revision: 30
  source_sha256: cc1296b53c6bfa489a562fa2b030b306a214ddcc05b08bb4e65122aeec2cd03a
  original_relations_sha256: 23a2dbb0032c678f99513dca03eeb9400f9ec18ffc71f4cec7b08a7e8f44541c
---
## Summary

Bind Project Settings **to** its authoritative TOML Carrier

## Claim

### Prose Claim


the authoritative TOML File Carrier for Project Settings of a Project named `<project_name>`.


the Project Settings Artifact for a Project named `<project_name>` **must** use `caprmedio_project_settings.toml` directly inside that selected Project's `.caprmedio_<project_name>/` control root as its **`=1`** authoritative TOML File Carrier.
