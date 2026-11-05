---
atom_id: CA-R-2793
current_scope_unit: WORKBENCH_CODEX
claim_target_scope_unit: WORKBENCH_CODEX
status: Archived
version: 1
author: Anatoly Maslennikov
role: Requirement
form: Entity Definition
tier: 3
subjects:
  active: CAPRMEDIO_MODEL <+ View
relations: {}
carrier_destination:
  file:
    name: CA-R-2793@1-WORKBENCH_CODEX-ENTITY_DEFINITION--define-view.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-47_FEATURE_WORKBENCH_CODEX/04_requirement/archive
updated_at: 2026-11-05 14:23:38 +0400
---

## Summary

Define View

## Claim

### Formal Claim

```CFEL
Workspace >{1+} View;
View.sql [string]{1};
View.name [string]{0..1}
```

### Prose Claim

A View is a Workbench SQL document in one Workspace. It has one SQL script and may have one name. Saving and loading a View are separate Workbench capabilities.
