---
atom_id: CA-R-2516
ref_id: CA-R-2516@6
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Requirement)/(.Header.Context.Form
    := Declaration)
tier: 3
status: archived
version: 6
updated_at: 2026-11-11 14:06:22 +0400
destination:
  file:
    name: CA-R-2516@6-CORE_META_MODEL-DECLARATION--declare-atom-role-requirement-form-declaration.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
---
## Summary

Declare Atom/(.Role := Requirement)/(.Form := Declaration)

## Claim

### Prose Claim


A Declaration states the applicable contract for its active Subject. Its Claim may contain several prose statements, CFEL formal expressions, or both when they form one coherent declaration about one topic.

Scope Unit Declaration is a Requirement Form using this template. It is not another Atom Role.

### Formal Claim

```CFEL
# model
Atom/(.Header.Context.Role in (Requirement)).Header.Context.Form :: Declaration;
```
