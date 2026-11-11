---
identity:
  atom_id: CA-R-2792
  ref_id: CA-R-2792
context:
  container:
    scope_unit: CA-SU-11
  role: Requirement
  form: Declaration
  topics:
    main_subject: MODEL//CAPRMEDIO <+ (Workspace, Workspace.native_thread_id, Workspace.project_root)
  tier: 3
state:
  status: Active
  version: 4
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-R-2792-CORE_META_MODEL-DECLARATION--define-workspace.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
author: Anatoly Maslennikov
---

## Summary

Define Workspace

## Claim

### Prose Claim

A Workspace is the Workbench context for one selected Project. In an existing native Codex chat, it binds to the host-supplied native thread reference; that reference is required only in native mode and is never invented or reused from another chat. In standalone browser mode, it uses the existing browser-owned Workspace/session ID without a native chat or an invented native thread reference. It keeps at least one View. It does not create a second conversation history or a standalone chat.
### Formal Claim

```CFEL
# model
Workspace.native_thread_id{::0..1}:: [string]{::0..1};
Workspace.project_root{::1}:: [string]{::1};
View {::1}((IS_CONTAINED_BY)){::1+} Workspace
```

