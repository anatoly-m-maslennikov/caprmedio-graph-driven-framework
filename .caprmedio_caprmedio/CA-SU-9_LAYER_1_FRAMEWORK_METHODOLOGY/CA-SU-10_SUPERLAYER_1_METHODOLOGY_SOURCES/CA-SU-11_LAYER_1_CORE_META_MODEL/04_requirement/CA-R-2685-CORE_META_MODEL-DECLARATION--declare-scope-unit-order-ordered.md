---
atom_id: CA-R-2685
ref_id: CA-R-2685
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit.order.ordered
  dependencies:
  - CAPRMEDIO_MODEL <+ Scope Unit.order
  - CAPRMEDIO_MODEL <+ CFEL <+ Format/bool
tier: 3
status: active
version: 2
updated_at: '2026-11-12T12:33:04.158402+00:00'
container:
  scope_unit: CA-SU-11
destination:
  file:
    name: CA-R-2685-CORE_META_MODEL-DECLARATION--declare-scope-unit-order-ordered.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare Scope Unit.order.ordered

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity

declare_entity(
    entity_name='ordered',
    relation_name='IS_PROPERTY_OF',
    base_path='Scope Unit.order',
    value_format=bool,
    value_cardinality=1,
    dependent_property_cardinality=0,
)
```

