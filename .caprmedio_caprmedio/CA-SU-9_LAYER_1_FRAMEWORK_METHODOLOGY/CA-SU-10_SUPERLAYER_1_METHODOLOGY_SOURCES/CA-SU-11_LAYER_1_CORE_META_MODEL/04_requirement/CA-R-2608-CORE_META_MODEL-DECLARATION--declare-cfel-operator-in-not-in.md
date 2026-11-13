---
atom_id: CA-R-2608
ref_id: CA-R-2608
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL<+Operator//Membership
tier: 3
status: active
version: 2
updated_at: '2026-11-13T05:29:16.220257+00:00'
carrier_destination:
  file:
    name: CA-R-2608-CORE_META_MODEL-DECLARATION--declare-cfel-operator-in-not-in.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---

## Summary

Declare CFEL operator in / not in

## Claim

### Formal Claim

```python
# model
set_value(address='Operator//Membership', value='"in / not in"')
```

## Semantics

Test membership or non-membership in a selected set.
