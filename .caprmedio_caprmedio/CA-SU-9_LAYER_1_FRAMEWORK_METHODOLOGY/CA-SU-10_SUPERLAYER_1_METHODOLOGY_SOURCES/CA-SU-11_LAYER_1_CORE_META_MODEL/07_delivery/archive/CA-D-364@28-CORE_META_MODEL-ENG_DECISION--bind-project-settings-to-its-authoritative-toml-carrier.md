---
subjects:
  governs: Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Settings
  depends_on:
  - Entity/Carrier/File.Filename
version: 28
updated_at: 2026-10-29 10:13:50 +0400
relations:
  child_of:
  - CA-D-363
atom_id: CA-D-364@28
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 5
type: Decision
---
## Summary

Bind Project Settings **to** its authoritative TOML Carrier

## Claim scope

the authoritative TOML File Carrier for Project Settings of a Project named `<project_name>`.

## Claim

the Project Settings Artifact for a Project named `<project_name>` **must** use `caprmedio_project_settings.toml` directly inside that selected Project's `.caprmedio_<project_name>/` control root as its **`=1`** authoritative TOML File Carrier.
