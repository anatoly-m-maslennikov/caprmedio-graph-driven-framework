---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Project.Settings
  passive:
  - CAPRMEDIO <+ MODEL <+ Carrier/File.Filename
version: 29
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-D-363
atom_id: CA-D-364
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 5
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-364-CORE_META_MODEL-ENG_DECISION--bind-project-settings-to-its-authoritative-toml-carrier.md
  source_atom_id: CA-D-364
  source_atom_revision: 29
  source_sha256: 843ca9bd746a595d68ddc2b791fe6a820657e98ae954bd5890886e366146c02f
  original_relations_sha256: 23a2dbb0032c678f99513dca03eeb9400f9ec18ffc71f4cec7b08a7e8f44541c
---
## Summary

Bind Project Settings **to** its authoritative TOML Carrier

## Claim scope

the authoritative TOML File Carrier for Project Settings of a Project named `<project_name>`.

## Claim

the Project Settings Artifact for a Project named `<project_name>` **must** use `caprmedio_project_settings.toml` directly inside that selected Project's `.caprmedio_<project_name>/` control root as its **`=1`** authoritative TOML File Carrier.
