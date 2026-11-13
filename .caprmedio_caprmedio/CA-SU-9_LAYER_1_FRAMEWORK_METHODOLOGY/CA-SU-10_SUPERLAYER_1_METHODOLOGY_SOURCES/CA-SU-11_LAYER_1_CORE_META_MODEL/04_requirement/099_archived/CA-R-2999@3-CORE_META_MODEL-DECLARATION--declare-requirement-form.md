---
atom_id: CA-R-2999
ref_id: CA-R-2999@3
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Form := Requirement)
tier: 3
status: archived
version: 3
updated_at: 2026-11-11 14:06:22 +0400
carrier_destination:
  file:
    name: CA-R-2999@3-CORE_META_MODEL-DECLARATION--declare-requirement-form.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
---

## Summary

Declare Requirement Form

## Claim

### Formal Claim

```CFEL
# model
Atom.Header.Context.Form :: Requirement;

# instances
FOR EACH $a[<Atom>, (.Header.Context.Form = Requirement)]:
(
    $a.Header.Context.Role:: [in (Requirement)]{::1}
)
```

## Semantics

A Requirement Form states a local required outcome, behavior, property or constraint.
