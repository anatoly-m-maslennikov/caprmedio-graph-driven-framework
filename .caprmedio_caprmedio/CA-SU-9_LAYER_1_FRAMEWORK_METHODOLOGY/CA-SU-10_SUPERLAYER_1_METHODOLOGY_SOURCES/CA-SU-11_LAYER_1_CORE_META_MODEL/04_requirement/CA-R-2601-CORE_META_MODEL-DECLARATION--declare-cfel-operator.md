---
atom_id: CA-R-2601
ref_id: CA-R-2601
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL<+Operator//Grouping
tier: 3
status: active
version: 4
updated_at: '2026-11-13T05:28:45.975735+00:00'
carrier_destination:
  file:
    name: CA-R-2601-CORE_META_MODEL-DECLARATION--declare-cfel-operator.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---

## Summary

Declare CFEL operator ()

## Claim

### Formal Claim

```python
# model
set_value(address='Operator//Grouping', value='"()"')
```

## Semantics

Group one CFEL expression; parentheses do not create a Node or Relation. When AND and OR occur in one Boolean expression, use parentheses to make their grouping explicit; neither has implicit precedence over the other.
