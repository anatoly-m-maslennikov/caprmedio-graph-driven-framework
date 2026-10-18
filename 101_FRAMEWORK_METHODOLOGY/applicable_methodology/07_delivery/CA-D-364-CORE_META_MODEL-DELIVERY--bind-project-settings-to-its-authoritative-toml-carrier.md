---
subjects:
  governs: "Entity/Continuant/Node/Project.Settings"
  depends_on:
    ["Entity/Carrier/File Carrier.Filename"]
version: 16
updated_at: "2026-10-18 07:37:54 +0400"
relations:
  child_of:
    - CA-D-363
atom_id: "CA-D-364"
content_role: "Delivery"
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-364-CORE_META_MODEL-DELIVERY--bind-project-settings-to-its-authoritative-toml-carrier.md
  source_atom_id: CA-D-364
  source_atom_revision: 16
  source_sha256: e51f690e81adf9d7edb65f4cd32c6ba74282b1944b132dab6b12022942b38c32
  original_relations_sha256: 5bb95efc70c0da210c80e3bdbc8549784b990261ebad7f7e71888cf52216ac85
---
# Summary

Bind Project Settings **to** its authoritative TOML Carrier

## Scope

the authoritative TOML File Carrier for Project Settings of a Project named `<project_name>`.

## Claim

the Project Settings Artifact for a Project named `<project_name>` **must** use `caprmedio_project_settings.toml` directly inside that selected Project's `.caprmedio_<project_name>/` control root as its **`=1`** authoritative TOML File Carrier.

## Details
