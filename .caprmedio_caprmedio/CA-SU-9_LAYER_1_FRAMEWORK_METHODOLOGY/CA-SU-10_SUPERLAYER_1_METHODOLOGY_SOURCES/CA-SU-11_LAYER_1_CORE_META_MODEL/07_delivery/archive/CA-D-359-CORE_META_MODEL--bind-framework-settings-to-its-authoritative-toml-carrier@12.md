---
subjects:
  governs: "Entity/Continuant/Object/Project.Framework Settings"
  depends_on:
    ["Entity/Carrier/File Carrier", "Entity/Carrier/File Carrier.Format"]
version: 12
updated_at: "2026-10-15 18:51:29 +0000"
relations:
  child_of:
    - CA-D-358
atom_id: "CA-D-359"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Bind Framework Settings to Its Authoritative TOML Carrier

## Scope

the Framework Instance Settings Artifact for a Project named `<project_name>`.

## Claim

the Framework Instance Settings Artifact for a Project named `<project_name>` **must** use `.caprmedio_<project_name>/000_CAPRMEDIO_framework/caprmedio_framework_settings.toml` as its **`=1`** authoritative TOML File Carrier.

## Details
