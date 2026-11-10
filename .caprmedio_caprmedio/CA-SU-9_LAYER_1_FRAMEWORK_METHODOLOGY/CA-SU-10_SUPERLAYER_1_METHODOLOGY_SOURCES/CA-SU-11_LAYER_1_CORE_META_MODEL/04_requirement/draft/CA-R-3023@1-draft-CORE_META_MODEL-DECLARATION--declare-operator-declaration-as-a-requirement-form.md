---
atom_id: CA-R-3023
ref_id: CA-R-3023@1-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form
    := Operator Declaration)
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)
tier: 3
status: Draft
version: 1
updated_at: 2026-11-10 22:09:03 +0400
carrier_destination:
  file:
    name: CA-R-3023@1-draft-CORE_META_MODEL-DECLARATION--declare-operator-declaration-as-a-requirement-form.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
---

## Summary

Declare Operator Declaration as a Requirement Form

## Claim

### Prose Claim

This Form uses the Declaration contract.

### Formal Claim

```CFEL
# model
Atom//(.Header.Role := Requirement).Header.Form := Operator Declaration;
Atom//(.Header.Role := Requirement)//(.Header.Form := Operator Declaration)
```

## Semantics

An Operator Declaration defines notation syntax and its operand rules.
