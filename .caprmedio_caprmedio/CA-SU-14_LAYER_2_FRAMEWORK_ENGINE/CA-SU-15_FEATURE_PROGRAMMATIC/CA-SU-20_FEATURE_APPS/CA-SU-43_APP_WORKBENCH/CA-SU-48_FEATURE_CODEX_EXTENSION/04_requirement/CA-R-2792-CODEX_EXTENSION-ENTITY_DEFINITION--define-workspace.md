---
identity:
  atom_id: CA-R-2792
  ref_id: CA-R-2792
context:
  container:
    scope_unit: CA-SU-48
  role: Requirement
  form: Entity Definition
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Workspace
  tier: 3
state:
  status: Active
  version: 3
  updated_at: 2026-11-09 00:09:26 +0400
destination:
  file:
    name: CA-R-2792-CODEX_EXTENSION-ENTITY_DEFINITION--define-workspace.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-48_FEATURE_CODEX_EXTENSION/04_requirement
current_scope_unit: CODEX_EXTENSION
claim_target_scope_unit: CODEX_EXTENSION
author: Anatoly Maslennikov
---

## Summary

Define Workspace

## Claim

### Prose Claim

A Workspace is the Workbench context for one selected Project. In an existing native Codex chat, it binds to the host-supplied native thread reference; that reference is required only in native mode and is never invented or reused from another chat. In standalone browser mode, it uses the existing browser-owned Workspace/session ID without a native chat or an invented native thread reference. It keeps at least one View. It does not create a second conversation history or a standalone chat.
### Formal Claim

```CFEL
Workspace.native_thread_id [string]{0..1};
Workspace.project_root [string]{1};
Workspace >{1+} View
```

