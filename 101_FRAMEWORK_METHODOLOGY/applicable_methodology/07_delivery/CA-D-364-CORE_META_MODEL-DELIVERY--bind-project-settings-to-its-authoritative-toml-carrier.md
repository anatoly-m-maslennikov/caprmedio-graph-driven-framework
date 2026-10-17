---
subjects:
  governs: "Entity/Continuant/Object/Project.Settings"
  depends_on:
    ["Entity/Carrier/File Carrier.Filename"]
version: 13
updated_at: "2026-10-16 12:09:22 +0000"
relations:
  child_of:
    - CA-D-363
atom_id: "CA-D-364"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-364-CORE_META_MODEL-DELIVERY--bind-project-settings-to-its-authoritative-toml-carrier.md
  source_atom_id: CA-D-364
  source_atom_revision: 13
  source_sha256: fcae88ed637cbc9f5d2941d21cdf658a2f43e3ef699edc89c5e7dd95d91635f6
  original_relations_sha256: 5bb95efc70c0da210c80e3bdbc8549784b990261ebad7f7e71888cf52216ac85
---
# Summary

Bind Project Settings **to** its authoritative TOML Carrier

## Scope

the authoritative TOML File Carrier for Project Settings of a Project named `<project_name>`.

## Claim

the Project Settings Artifact for a Project named `<project_name>` **must** use `caprmedio_project_settings.toml` directly inside that selected Project's `.caprmedio_<project_name>/` control root as its **`=1`** authoritative TOML File Carrier.

## Details
