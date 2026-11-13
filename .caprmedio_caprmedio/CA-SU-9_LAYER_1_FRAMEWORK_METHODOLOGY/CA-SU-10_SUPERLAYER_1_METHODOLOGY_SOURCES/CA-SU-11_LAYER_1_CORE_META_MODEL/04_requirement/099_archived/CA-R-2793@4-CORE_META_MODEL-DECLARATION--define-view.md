---
identity:
  atom_id: CA-R-2793
  ref_id: CA-R-2793@4
context:
  container:
    scope_unit: CA-SU-11
  role: Requirement
  form: Declaration
  topics:
    main_subject: MODEL//CAPRMEDIO <+ (View, View.id, View.sql, View.name)
  tier: 3
state:
  status: archived
  version: 4
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-R-2793@4-CORE_META_MODEL-DECLARATION--define-view.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
author: Anatoly Maslennikov
---

## Summary

Define View

## Claim

### Prose Claim

A View is a Workbench SQL document in one Workspace. It has one stable string ID, one complete SQL query and may have one name. A View can be edited, run, fetched, focused, renamed, removed or saved through the Workspace operations.
### Formal Claim

```CFEL
# model
View.id{::1}:: [string]{::1};
View.sql{::1}:: [string]{::1};
View.name{::0..1}:: [string]{::0..1}
```

