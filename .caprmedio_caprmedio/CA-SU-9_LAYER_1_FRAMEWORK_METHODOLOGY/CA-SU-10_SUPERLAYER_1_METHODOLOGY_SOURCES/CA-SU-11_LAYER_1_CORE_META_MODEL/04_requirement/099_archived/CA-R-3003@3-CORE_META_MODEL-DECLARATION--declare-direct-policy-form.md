---
atom_id: CA-R-3003
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Form := Direct Policy)
tier: 3
ref_id: CA-R-3003@3
status: archived
version: 3
updated_at: 2026-11-11 14:06:22 +0400
carrier_destination:
  file:
    name: CA-R-3003@3-CORE_META_MODEL-DECLARATION--declare-direct-policy-form.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
---

## Summary

Declare Direct Policy Form

## Claim

### Formal Claim

```CFEL
# model
Atom.Header.Context.Form :: Direct Policy;

# instances
FOR EACH $a[<Atom>, (.Header.Context.Form = Direct Policy)]:
(
    $a.Header.Context.Role:: [in (Requirement, Method, Evaluation, Delivery, Operations)]{::1}
)
```

## Semantics

A Direct Policy applies to all descendants recursively without a local copy. A genuine SPECIALIZES Atom may add applicable detail while preserving parent constraints.
