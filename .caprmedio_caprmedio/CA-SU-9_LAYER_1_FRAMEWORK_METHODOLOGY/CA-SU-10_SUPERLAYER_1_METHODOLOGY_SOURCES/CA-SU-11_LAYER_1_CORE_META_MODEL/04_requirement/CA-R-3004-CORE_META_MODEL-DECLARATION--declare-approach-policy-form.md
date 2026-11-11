---
atom_id: CA-R-3004
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Form := Approach Policy)
tier: 3
ref_id: CA-R-3004
status: Active
version: 3
updated_at: '2026-11-11 14:06:22 +0400'
carrier_destination:
  file:
    name: CA-R-3004-CORE_META_MODEL-DECLARATION--declare-approach-policy-form.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---

## Summary

Declare Approach Policy Form

## Claim

### Formal Claim

```CFEL
# model
Atom.Header.Context.Form :: Approach Policy;

# instances
FOR EACH $a[<Atom>, (.Header.Context.Form = Approach Policy)]:
(
    $a.Header.Context.Role:: [in (Requirement, Method, Evaluation, Delivery, Operations)]{::1}
)
```

## Semantics

An Approach Policy is conditional on its stated case. At every descendant where that case applies, a local Atom must bind the Policy to the actual case through SPECIALIZES. A reference alone is insufficient; the binding preserves parent constraints.
