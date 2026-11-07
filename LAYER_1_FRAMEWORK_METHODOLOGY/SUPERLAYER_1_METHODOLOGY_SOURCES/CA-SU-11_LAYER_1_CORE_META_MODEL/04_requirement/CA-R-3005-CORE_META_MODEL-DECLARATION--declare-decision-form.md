---
atom_id: CA-R-3005
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Form := Decision)
tier: 3
ref_id: CA-R-3005
status: Active
version: 2
updated_at: "2026-11-07 15:18:44 +0400"
carrier_destination:
  file:
    name: CA-R-3005-CORE_META_MODEL-DECLARATION--declare-decision-form.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---

## Summary

Declare Decision Form

## Claim

### Formal Claim

```CFEL
# model
Atom/(.Header.Form := Decision);

# instances
Atom/(.Header.Form := Decision)//$decision.Header.Role:: [in (Method, Evaluation, Delivery, Operations)]{::1}
```

## Semantics

A Decision records a particular local choice. Applicable governing constraints continue to apply.
