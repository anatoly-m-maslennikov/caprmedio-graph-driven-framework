---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Settings
  depends_on:
  - Subject/CAPRMEDIO/Carrier/File.Filename
version: 25
updated_at: 2026-10-27 19:59:24 +0400
relations:
  child_of:
  - CA-D-363
atom_id: CA-D-364
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 5
type: Eng Decision
---
# Summary

Bind Project Settings **to** its authoritative TOML Carrier

## Scope

the authoritative TOML File Carrier for Project Settings of a Project named `<project_name>`.

## Claim

the Project Settings Artifact for a Project named `<project_name>` **must** use `caprmedio_project_settings.toml` directly inside that selected Project's `.caprmedio_<project_name>/` control root as its **`=1`** authoritative TOML File Carrier.

## Details
