---
subjects:
  active: CAPRMEDIO_MODEL <+ Project.Settings
  passive:
  - CAPRMEDIO_MODEL <+ Carrier/File
version: 30
updated_at: 2026-11-03 23:25:51 +0400
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
---
## Summary

Bind Project Settings **to** its authoritative TOML Carrier

## Claim

### Prose Claim


the authoritative TOML File Carrier for Project Settings of a Project named `<project_name>`.


the Project Settings Artifact for a Project named `<project_name>` **must** use `caprmedio_project_settings.toml` directly inside that selected Project's `.caprmedio_<project_name>/` control root as its **`=1`** authoritative TOML File Carrier.
