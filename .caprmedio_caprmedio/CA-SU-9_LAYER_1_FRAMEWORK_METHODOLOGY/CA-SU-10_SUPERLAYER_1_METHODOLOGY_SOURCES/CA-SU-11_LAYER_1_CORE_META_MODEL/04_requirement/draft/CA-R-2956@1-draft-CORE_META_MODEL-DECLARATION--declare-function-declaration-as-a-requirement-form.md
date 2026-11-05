---
atom_id: CA-R-2956
ref_id: CA-R-2956@1-draft
status: Draft
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Function Declaration)
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)
tier: 3
role: Requirement
form: Declaration
version: 1
updated_at: 2026-11-05 19:15:20 +0400
carrier_destination:
  file:
    name: CA-R-2956@1-draft-DECLARATION--declare-function-declaration-as-a-requirement-form.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
container:
  scope_unit: CA-SU-11
---

## Summary

Declare Function Declaration as a Requirement Form

## Claim

### Formal Claim

```CFEL
# model
Atom//(.Header.Role := Requirement).Header.Form := Function Declaration;
Atom//(.Header.Role := Requirement)//(.Header.Form := Function Declaration)
```

### Prose Claim

This Form uses the Declaration contract.

## Semantics

A Function Declaration defines a pure function signature, including its input and output Formats; a predicate returns Bool.
