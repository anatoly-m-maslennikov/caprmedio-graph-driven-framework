---
atom_id: CA-R-3002
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Form := Solution)
tier: 3
ref_id: CA-R-3002
status: Active
version: 3
updated_at: '2026-11-11 14:06:22 +0400'
carrier_destination:
  file:
    name: CA-R-3002-CORE_META_MODEL-DECLARATION--declare-solution-form.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---

## Summary

Declare Solution Form

## Claim

### Formal Claim

```CFEL
# model
Atom.Header.Context.Form :: Solution;

# instances
FOR EACH $a[<Atom>, (.Header.Context.Form = Solution)]:
(
    $a.Header.Context.Role:: [in (Requirement, Method, Evaluation, Delivery, Operations)]{::1}
)
```

## Semantics

A Solution specifies the contribution that realizes a Scope Unit’s responsibility across the unit and its descendants. Its Role identifies the contribution.
