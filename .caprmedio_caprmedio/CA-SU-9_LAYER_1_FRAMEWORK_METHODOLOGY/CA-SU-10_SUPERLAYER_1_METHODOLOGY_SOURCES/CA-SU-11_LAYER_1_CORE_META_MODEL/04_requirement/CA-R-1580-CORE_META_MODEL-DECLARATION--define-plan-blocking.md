---
atom_id: CA-R-1580
ref_id: CA-R-1580
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//BLOCKS
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan)/(.Header.Context.Form :=
    Plan)
  - CAPRMEDIO_MODEL <+ Projection
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan).Header.State.Status: Done'
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//DEPENDS_ON
tier: 1
status: active
version: 30
updated_at: '2026-11-13T06:26:07.833706+00:00'
carrier_destination:
  file:
    name: CA-R-1580-CORE_META_MODEL-DECLARATION--define-plan-blocking.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Define Plan blocking

## Claim

### Formal Claim

```python
# model
relation(source='Relation//BLOCKS', name='HAS_INVERSE', target='Relation//IS_BLOCKED_BY', reverse=True)
classify(address='Relation//BLOCKS', axis='Derivation', value='Derived', notation='relation')
# instances
relation(source='Atom/(.Header.Context.Role: Plan)//$prerequisite', name='BLOCKS', target='Atom/(.Header.Context.Role: Plan)//$dependent')
```

## Semantics

BLOCKS relates a prerequisite Plan to a dependent Plan that may start only after that prerequisite is Done.
