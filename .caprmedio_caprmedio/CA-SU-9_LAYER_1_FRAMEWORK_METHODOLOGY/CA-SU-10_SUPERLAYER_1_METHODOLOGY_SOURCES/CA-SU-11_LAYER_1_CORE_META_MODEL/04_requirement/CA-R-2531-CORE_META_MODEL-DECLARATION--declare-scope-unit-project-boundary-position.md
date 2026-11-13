---
atom_id: CA-R-2531
ref_id: CA-R-2531
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit.Project Boundary Position
tier: 3
status: active
version: 3
updated_at: '2026-11-12T17:23:54+00:00'
carrier_destination:
  file:
    name: CA-R-2531-CORE_META_MODEL-DECLARATION--declare-scope-unit-project-boundary-position.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---

## Summary

Declare Scope Unit Project Boundary Position

## Claim

### Formal Claim

```python
# model
from caprmedio.formal_claims import declare_entity

declare_entity(
    entity_name='Project Boundary Position',
    relation_name='IS_PROPERTY_OF',
    base_path='Scope Unit',
    property_occurrence_cardinality=1,
    value_cardinality=1,
    value_format='str',
    dependent_property_cardinality=0,
)
```

