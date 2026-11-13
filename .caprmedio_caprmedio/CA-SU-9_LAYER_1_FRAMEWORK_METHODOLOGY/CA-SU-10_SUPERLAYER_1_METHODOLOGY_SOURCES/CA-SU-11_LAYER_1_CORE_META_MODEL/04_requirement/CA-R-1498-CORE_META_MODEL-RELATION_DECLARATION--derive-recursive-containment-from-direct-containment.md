---
atom_id: CA-R-1498
ref_id: CA-R-1498
container:
  scope_unit: CA-SU-11
role: Requirement
form: Relation Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//RECURSIVELY_CONTAINS
  dependencies:
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//CONTAINS
tier: 1
status: active
version: 19
updated_at: '2026-11-13T08:13:26.277090+00:00'
carrier_destination:
  file:
    name: CA-R-1498-CORE_META_MODEL-RELATION_DECLARATION--derive-recursive-containment-from-direct-containment.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Derive Recursive Containment from Direct Containment

## Claim

### Formal Claim

```python
# model
relation(source='$container', name='RECURSIVELY_CONTAINS', target='$descendant')
classify(address='Relation//RECURSIVELY_CONTAINS', axis='Derivation', value='Derived', notation='relation')
```

## Semantics

The Host recursively contains the Target when one or more successive `CONTAINS` links lead from Host to Target. Intermediate Entities need only satisfy the endpoint constraints of `CONTAINS`. Derive this Relation from the existing links.
