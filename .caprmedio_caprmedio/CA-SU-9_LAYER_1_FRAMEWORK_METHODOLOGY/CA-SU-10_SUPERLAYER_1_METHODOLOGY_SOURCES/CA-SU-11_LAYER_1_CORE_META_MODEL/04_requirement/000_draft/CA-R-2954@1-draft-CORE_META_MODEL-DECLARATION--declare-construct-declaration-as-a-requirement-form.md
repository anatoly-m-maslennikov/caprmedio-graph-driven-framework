---
atom_id: CA-R-2954
ref_id: CA-R-2954@1-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Requirement)/(.Header.Context.Form := Construct Declaration)
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Requirement)
tier: 3
status: Draft
version: 1
updated_at: 2026-11-05 19:15:20 +0400
carrier_destination:
  file:
    name: CA-R-2954@1-draft-DECLARATION--declare-construct-declaration-as-a-requirement-form.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft
---

## Summary

Declare Construct Declaration as a Requirement Form

## Claim

### Prose Claim

This Form uses the Declaration contract.

### Formal Claim

```CFEL
# model
Atom/(.Header.Context.Role in (Requirement)).Header.Context.Form :: Construct Declaration;

Atom/(.Header.Context.Role in (Requirement))/(.Header.Context.Form in (Construct Declaration))
```

## Semantics

A Construct Declaration defines the structure and binding scope of a multi-expression language construct.
