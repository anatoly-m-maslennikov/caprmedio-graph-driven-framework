---
atom_id: CA-R-2793
current_scope_unit: CODEX_EXTENSION
claim_target_scope_unit: CODEX_EXTENSION
status: Active
version: 2
author: Anatoly Maslennikov
role: Requirement
form: Entity Definition
tier: 3
subjects:
  active: CAPRMEDIO_MODEL <+ View
relations: {}
carrier_destination:
  file:
    name: CA-R-2793-CODEX_EXTENSION-ENTITY_DEFINITION--define-view.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-48_FEATURE_CODEX_EXTENSION/04_requirement
updated_at: 2026-11-05 16:45:35 +0400
---

## Summary

Define View

## Claim

### Formal Claim

```CFEL
Workspace >{1+} View;
View.id [string]{1};
View.sql [string]{1};
View.name [string]{0..1}
```

### Prose Claim

A View is a Workbench SQL document in one Workspace. It has one stable string ID, one SQL script and may have one name. A View can be edited, run, fetched, focused, renamed, removed or saved through the Workspace operations.
