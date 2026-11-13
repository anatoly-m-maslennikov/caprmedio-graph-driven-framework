---
atom_id: CA-R-2650
ref_id: CA-R-2650@3
role: Requirement
form: Scope Delegation
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//CORE_META_MODEL
tier: 3
status: archived
version: 3
updated_at: 2026-11-10 20:52:03 +0400
destination:
  file:
    name: CA-R-2650@3-METHODOLOGY_SOURCES-DEFINES_SCOPE_FOR-CORE_META_MODEL--declare-core-meta-model.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/04_requirement/099_archived
author: Anatoly Maslennikov
container:
  scope_unit: CA-SU-10
---
## Summary

Declare CORE_META_MODEL

## Claim


### Prose Claim

Additional HAS_ACTIVE_SUBJECT permissions for local Atoms in CORE_META_MODEL are exactly these finite typed selections:

- `MODEL//CAPRMEDIO <+ (Workspace, Workspace.native_thread_id, Workspace.project_root)`;
- `MODEL//CAPRMEDIO <+ (View, View.id, View.sql, View.name)`;



No unlisted descendants or other type members are admitted. An unresolved address grants no admission.


The Workspace and View grouped selections enumerate only the endpoint and Property objects declared by R2792 and R2793. These finite selections admit no other descendants or type members. Their Declaration ownership includes exactly those listed objects.

### Formal Claim

```CFEL
# instances
Scope Unit//CORE_META_MODEL.ID == "CA-SU-11";

Scope Unit//CORE_META_MODEL.Name == "CORE_META_MODEL";

Scope Unit//CORE_META_MODEL.Label == "LAYER";

Scope Unit//CORE_META_MODEL.order.ordered == true;

Scope Unit//CORE_META_MODEL.order.number == 1;

Scope Unit//CORE_META_MODEL ((IS_CONTAINED_BY)) Scope Unit//METHODOLOGY_SOURCES
```
