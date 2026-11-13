---
atom_id: CA-R-2761
ref_id: CA-R-2761@1-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_PRODUCED_BY
tier: 1
status: Draft
version: 1
updated_at: 2026-11-04 16:07:35 +0400
carrier_destination:
  file:
    name: CA-R-2761@1-draft-CORE_META_MODEL-DECLARATION--declare-is-produced-by.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft
---
## Summary

Declare IS_PRODUCED_BY

## Claim

### Formal Claim

```python
# model
relation(source='Relation//IS_PRODUCED_BY', name='HAS_INVERSE', target='Relation//PRODUCES', reverse=True)
classify(address='Relation//IS_PRODUCED_BY', axis='Derivation', value='Derived', notation='relation')
# instances
relation(source='Event//$event', name='IS_PRODUCED_BY', target='Execution//$execution')
```

## Semantics

IS_PRODUCED_BY links an Event to an Execution that produced it.
