---
atom_id: CA-R-3003
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Form := Direct Policy)
tier: 3
ref_id: CA-R-3003
status: Active
version: 2
updated_at: "2026-11-07 15:18:44 +0400"
carrier_destination:
  file:
    name: CA-R-3003-CORE_META_MODEL-DECLARATION--declare-direct-policy-form.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---

## Summary

Declare Direct Policy Form

## Claim

### Formal Claim

```CFEL
# model
Atom/(.Header.Form := Direct Policy);

# instances
Atom/(.Header.Form := Direct Policy)//$direct_policy.Header.Role:: [in (Requirement, Method, Evaluation, Delivery, Operations)]{::1}
```

## Semantics

A Direct Policy applies to all descendants recursively without a local copy. A genuine SPECIALIZES Atom may add applicable detail while preserving parent constraints.
