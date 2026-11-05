---
atom_id: CA-R-2792
ref_id: CA-R-2792
current_scope_unit: CODEX_EXTENSION
claim_target_scope_unit: CODEX_EXTENSION
status: Active
version: 2
author: Anatoly Maslennikov
role: Requirement
form: Entity Definition
tier: 3
topics:
  main_subject: CAPRMEDIO_MODEL <+ Workspace
carrier_destination:
  file:
    name: CA-R-2792-CODEX_EXTENSION-ENTITY_DEFINITION--define-workspace.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-48_FEATURE_CODEX_EXTENSION/04_requirement
updated_at: 2026-11-05 16:45:35 +0400
container:
  scope_unit: CA-SU-48
---

## Summary

Define Workspace

## Claim

### Formal Claim

```CFEL
Workspace.native_thread_id [string]{1};
Workspace.project_root [string]{1};
Workspace >{1+} View
```

### Prose Claim

A Workspace is the Workbench context for one existing native Codex chat in one selected Project. It keeps one native thread reference and at least one View. It does not create a second conversation history or a standalone chat.
