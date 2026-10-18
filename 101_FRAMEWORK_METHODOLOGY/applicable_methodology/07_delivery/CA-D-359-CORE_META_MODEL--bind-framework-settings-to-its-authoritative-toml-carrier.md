---
subjects:
  governs: "Entity/Continuant/Node/Project.Framework Settings"
  depends_on:
    ["Entity/Carrier/File Carrier", "Entity/Carrier/File Carrier.Format"]
version: 15
updated_at: "2026-10-18 07:37:23 +0400"
relations:
  child_of:
    - CA-D-358
atom_id: "CA-D-359"
content_role: "Delivery"
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-359-CORE_META_MODEL--bind-framework-settings-to-its-authoritative-toml-carrier.md
  source_atom_id: CA-D-359
  source_atom_revision: 15
  source_sha256: 60eed24afdcc745fffe69acbb438db7f1f806c0007c6995c52fb615411eadbf7
  original_relations_sha256: 48bb8e84d64eff4539728a3dc750fab3055957a8021a42380f1a6137ce28526a
---
# Summary

Bind Framework Settings to Its Authoritative TOML Carrier

## Scope

the Framework Instance Settings Artifact for a Project named `<project_name>`.

## Claim

the Framework Instance Settings Artifact for a Project named `<project_name>` **must** use `.caprmedio_<project_name>/000_CAPRMEDIO_framework/caprmedio_framework_settings.toml` as its **`=1`** authoritative TOML File Carrier.

## Details
