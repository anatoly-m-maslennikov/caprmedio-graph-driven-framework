---
atom_id: CA-R-2955
ref_id: CA-R-2955@2
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Requirement)/(.Header.Context.Form
    := Relation Declaration)
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Requirement)
tier: 3
status: archived
version: 2
updated_at: 2026-11-11 14:06:22 +0400
carrier_destination:
  file:
    name: CA-R-2955@2-CORE_META_MODEL-DECLARATION--declare-relation-declaration-as-a-requirement-form.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
---

## Summary

Declare Relation Declaration as a Requirement Form

## Claim

### Prose Claim

This Form uses the Declaration contract.

### Formal Claim

```CFEL
# model
Atom/(.Header.Context.Role in (Requirement)).Header.Context.Form :: Relation Declaration;
```

## Semantics

A Relation Declaration defines a canonical binary Relation, its endpoint domains and applicable inverse aliases.
