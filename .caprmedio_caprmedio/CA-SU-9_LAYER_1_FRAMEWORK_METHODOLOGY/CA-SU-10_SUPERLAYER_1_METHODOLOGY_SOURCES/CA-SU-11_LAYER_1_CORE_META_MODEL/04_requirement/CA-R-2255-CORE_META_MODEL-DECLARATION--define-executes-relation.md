---
atom_id: CA-R-2255
ref_id: CA-R-2255
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//EXECUTES
  dependencies:
  - CAPRMEDIO_MODEL <+ Runtime
  - CAPRMEDIO_MODEL <+ Execution
tier: 1
status: active
version: 10
updated_at: 2026-11-05 03:46:06 +0400
carrier_destination:
  file:
    name: CA-R-2255-CORE_META_MODEL-DECLARATION--define-executes-relation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Define EXECUTES Relation

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_relation

declare_relation(
    relation_name='EXECUTES',
    source_endpoint={"level": "instances", "entity_paths": ('Runtime',)},
    target_endpoint={"level": "instances", "entity_paths": ('Execution',)},
    inverse_alias='IS_EXECUTED_BY',
)
```

## Semantics

EXECUTES is the stored Relation from a Runtime to an Execution. Its declared inverse IS_EXECUTED_BY is a derived view.
