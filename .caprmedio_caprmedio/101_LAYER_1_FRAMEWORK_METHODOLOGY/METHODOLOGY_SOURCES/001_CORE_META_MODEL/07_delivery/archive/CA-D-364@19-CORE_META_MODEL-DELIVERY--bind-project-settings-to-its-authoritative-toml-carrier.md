---
subjects:
  governs: Subject/Domain/Node/Continuant/Project.Settings
  depends_on:
  - Subject/Engineering/Carrier/File Carrier.Filename
version: 19
updated_at: 2026-10-24 00:38:25 +0400
relations:
  child_of:
  - CA-D-363
atom_id: CA-D-364@19
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
---
# Summary

Bind Project Settings **to** its authoritative TOML Carrier

## Scope

the authoritative TOML File Carrier for Project Settings of a Project named `<project_name>`.

## Claim

the Project Settings Artifact for a Project named `<project_name>` **must** use `caprmedio_project_settings.toml` directly inside that selected Project's `.caprmedio_<project_name>/` control root as its **`=1`** authoritative TOML File Carrier.

## Details
