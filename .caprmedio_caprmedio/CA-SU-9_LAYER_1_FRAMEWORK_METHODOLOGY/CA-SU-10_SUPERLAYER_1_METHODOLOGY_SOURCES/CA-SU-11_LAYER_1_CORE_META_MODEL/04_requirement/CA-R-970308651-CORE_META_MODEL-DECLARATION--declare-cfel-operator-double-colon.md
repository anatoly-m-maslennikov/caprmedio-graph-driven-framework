---
atom_id: CA-R-970308651
ref_id: CA-R-970308651
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL<+Operator//AllowedValue
tier: 3
relations:
  is_replacement_for:
  - CA-R-2592
status: Active
version: 1
updated_at: '2026-11-11 14:06:22 +0400'
carrier_destination:
  file:
    name: CA-R-970308651-CORE_META_MODEL-DECLARATION--declare-cfel-operator-double-colon.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---

## Summary

Declare CFEL operator ::

## Claim

### Formal Claim

```CFEL
# model
Operator//AllowedValue == "::"
```

## Semantics

In `X :: Y`, a literal Y admits one allowed value of the complete qualified Property address X. A bracketed right operand supplies a Format constraint.
