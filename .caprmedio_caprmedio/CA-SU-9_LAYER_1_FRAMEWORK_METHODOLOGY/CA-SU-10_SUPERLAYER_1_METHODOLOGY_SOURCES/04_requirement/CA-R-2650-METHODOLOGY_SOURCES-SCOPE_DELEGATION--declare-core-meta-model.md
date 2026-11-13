---
atom_id: CA-R-2650
ref_id: CA-R-2650
role: Requirement
form: Scope Delegation
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//CORE_META_MODEL
tier: 3
status: active
version: 4
updated_at: '2026-11-13T07:29:43.184787+00:00'
destination:
  file:
    name: CA-R-2650-METHODOLOGY_SOURCES-SCOPE_DELEGATION--declare-core-meta-model.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/04_requirement
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

