---
atom_id: CA-R-2586
ref_id: CA-R-2586
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection.Source
tier: 3
status: active
version: 3
updated_at: '2026-11-12T17:23:54+00:00'
carrier_destination:
  file:
    name: CA-R-2586-CORE_META_MODEL-DECLARATION--declare-projection-source.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare Projection.Source

## Claim

### Formal Claim

```python
# model
from caprmedio.formal_claims import Cardinality, declare_entity

declare_entity(
    entity_name='Source',
    relation_name='IS_PROPERTY_OF',
    base_path='Projection',
    property_occurrence_cardinality=1,
    value_cardinality=0,
    dependent_property_cardinality=Cardinality(minimum=1, maximum=2),
    allowed_dependent_property_names=('Named Selection', 'Atoms'),
)
```

