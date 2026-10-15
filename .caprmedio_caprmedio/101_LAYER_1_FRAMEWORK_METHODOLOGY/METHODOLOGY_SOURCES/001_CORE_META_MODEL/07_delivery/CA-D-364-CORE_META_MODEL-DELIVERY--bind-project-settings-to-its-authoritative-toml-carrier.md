---
subjects:
  governs: "Entity/Continuant/Object/Project.Settings"
  depends_on:
    ["Project Settings Authoritative TOML File Carrier.Filename"]
version: 12
updated_at: "2026-10-15 18:51:33 +0000"
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
---
# Summary

Bind Project Settings **to** its authoritative TOML Carrier

## Scope

the authoritative TOML File Carrier for Project Settings of a Project named `<project_name>`.

## Claim

the Project Settings Artifact for a Project named `<project_name>` **must** use `caprmedio_project_settings.toml` directly inside that selected Project's `.caprmedio_<project_name>/` control root as its **`=1`** authoritative TOML File Carrier.

## Details
