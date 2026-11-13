---
atom_id: CA-R-2687
ref_id: CA-R-2687
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit.order
  dependencies:
  - CAPRMEDIO_MODEL <+ Scope Unit
tier: 3
status: active
version: 2
updated_at: '2026-11-13T00:35:42.536630+00:00'
container:
  scope_unit: CA-SU-11
destination:
  file:
    name: CA-R-2687-CORE_META_MODEL-DECLARATION--declare-scope-unit-order.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare Scope Unit.order

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import Cardinality, declare_entity

declare_entity(
    entity_name="order",
    relation_name="IS_PROPERTY_OF",
    base_path="Scope Unit",
    value_cardinality=0,
    dependent_property_cardinality=Cardinality(minimum=1, maximum=2),
    allowed_dependent_property_names=("ordered", "number"),
)
```

## Semantics

order groups the Boolean ordered and the conditional number as sibling Properties. The group has no direct value.
