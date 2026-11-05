---
atom_id: CA-R-2792
current_scope_unit: WORKBENCH_CODEX
claim_target_scope_unit: WORKBENCH_CODEX
status: Archived
version: 1
author: Anatoly Maslennikov
role: Requirement
form: Entity Definition
tier: 3
subjects:
  active: CAPRMEDIO_MODEL <+ Workspace
relations: {}
carrier_destination:
  file:
    name: CA-R-2792@1-WORKBENCH_CODEX-ENTITY_DEFINITION--define-workspace.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-47_FEATURE_WORKBENCH_CODEX/04_requirement/archive
updated_at: 2026-11-05 14:23:38 +0400
---

## Summary

Define Workspace

## Claim

### Formal Claim

```CFEL
Project >{1} Workspace;
Workspace.chat_thread_id [string]{1};
Workspace >{1+} View
```

### Prose Claim

A Workspace is the Project's persistent Workbench context. In this MVP, each Project has exactly one Workspace. The Workspace has exactly one reference to that Project's native persisted app-server thread and one or more Views.

Workspace does not redefine the global Session entity. Multiple Workspace management is out of scope.
