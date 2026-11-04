---
atom_id: CA-R-2769
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL<+Operator//Fallback
version: 2
updated_at: 2026-11-04 20:33:16 +0400
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
tier: 3
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2769-CORE_META_MODEL-DECLARATION--declare-cfel-operator.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---

## Summary

Declare CFEL operator ?==

## Claim

### Formal Claim

```CFEL
# model
Operator//Fallback == "?=="
```

## Semantics

Conditionally assign the first available valid value to a missing Object Property in the Model. This does not itself write a Carrier; persistence is the responsibility of an adapter or Delivery rule.
