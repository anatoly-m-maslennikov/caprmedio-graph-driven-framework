---
atom_id: CA-R-2612
ref_id: CA-R-2612
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL<+Operator//RecursiveWildcard
tier: 3
status: active
version: 2
updated_at: '2026-11-13T05:29:29.795188+00:00'
carrier_destination:
  file:
    name: CA-R-2612-CORE_META_MODEL-DECLARATION--declare-cfel-operator.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---

## Summary

Declare CFEL operator **

## Claim

### Formal Claim

```python
# model
set_value(address='Operator//RecursiveWildcard', value='"**"')
```

## Semantics

Select distinct dependent Property identities recursively below p in one bearer.
A `p.**` count aggregates that selection across all descendant depths; it does
not count values or another bearer's selection.
