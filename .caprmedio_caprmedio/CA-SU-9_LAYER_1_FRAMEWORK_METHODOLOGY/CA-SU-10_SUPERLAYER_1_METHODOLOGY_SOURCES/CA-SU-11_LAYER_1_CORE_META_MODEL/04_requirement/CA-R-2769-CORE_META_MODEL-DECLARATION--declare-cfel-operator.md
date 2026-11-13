---
atom_id: CA-R-2769
ref_id: CA-R-2769
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL<+Operator//Fallback
tier: 3
status: active
version: 3
updated_at: '2026-11-13T05:29:46.380727+00:00'
carrier_destination:
  file:
    name: CA-R-2769-CORE_META_MODEL-DECLARATION--declare-cfel-operator.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---

## Summary

Declare CFEL operator ?==

## Claim

### Formal Claim

```python
# model
set_value(address='Operator//Fallback', value='"?=="')
```

## Semantics

Conditionally assign the first available valid value to a missing Object Property in the Model. This does not itself write a Carrier; persistence is the responsibility of an adapter or Delivery rule.
