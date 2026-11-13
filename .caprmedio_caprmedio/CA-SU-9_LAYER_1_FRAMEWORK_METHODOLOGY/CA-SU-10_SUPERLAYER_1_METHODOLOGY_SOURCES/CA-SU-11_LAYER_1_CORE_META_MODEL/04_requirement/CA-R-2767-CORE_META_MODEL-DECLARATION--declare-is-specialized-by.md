---
atom_id: CA-R-2767
ref_id: CA-R-2767
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_SPECIALIZED_BY
tier: 1
status: active
version: 3
updated_at: '2026-11-13T05:43:15.642252+00:00'
carrier_destination:
  file:
    name: CA-R-2767-CORE_META_MODEL-DECLARATION--declare-is-specialized-by.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare IS_SPECIALIZED_BY

## Claim

### Formal Claim

```python
# model
relation(source='Relation//IS_SPECIALIZED_BY', name='HAS_INVERSE', target='Relation//SPECIALIZES', reverse=True)
classify(address='Relation//IS_SPECIALIZED_BY', axis='Derivation', value='Derived', notation='relation')
# instances
relation(source='Atom//$parent', name='IS_SPECIALIZED_BY', target='Atom//$child')
```

## Semantics

IS_SPECIALIZED_BY relates an Atom to an Atom whose Claim specializes its Claim.
