---
atom_id: CA-R-2420
ref_id: CA-R-2420@6-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_EXECUTED_BY
tier: 1
status: Draft
version: 6
updated_at: 2026-11-04 16:07:35 +0400
carrier_destination:
  file:
    name: CA-R-2420@6-draft-CORE_META_MODEL-DECLARATION--define-is-executed-by-relation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft
---
## Summary

Define IS_EXECUTED_BY Relation

## Claim

### Formal Claim

```python
# model
relation(source='Relation//IS_EXECUTED_BY', name='HAS_INVERSE', target='Relation//EXECUTES', reverse=True)
classify(address='Relation//IS_EXECUTED_BY', axis='Derivation', value='Derived', notation='relation')
# instances
relation(source='Execution//$execution', name='IS_EXECUTED_BY', target='Runtime//$runtime')
```

## Semantics

IS_EXECUTED_BY is the derived view from an Execution to a Runtime of the stored EXECUTES fact.
