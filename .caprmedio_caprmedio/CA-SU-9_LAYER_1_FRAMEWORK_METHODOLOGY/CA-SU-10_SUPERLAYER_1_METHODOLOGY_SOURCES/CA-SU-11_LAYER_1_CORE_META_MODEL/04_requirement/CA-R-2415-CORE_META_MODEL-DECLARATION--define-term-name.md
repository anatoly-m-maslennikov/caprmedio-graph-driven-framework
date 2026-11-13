---
atom_id: CA-R-2415
ref_id: CA-R-2415
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Term.Name
tier: 1
status: active
version: 5
updated_at: '2026-11-12T17:23:54+00:00'
carrier_destination:
  file:
    name: CA-R-2415-CORE_META_MODEL-DECLARATION--define-term-name.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Term Name

## Claim

### Prose Claim

Term.Name is the required word or phrase used as the Term's meaning.
### Formal Claim

```python
# model
from caprmedio.formal_claims import declare_entity

declare_entity(
    entity_name='Name',
    relation_name='IS_PROPERTY_OF',
    base_path='Term',
    property_occurrence_cardinality=1,
    value_cardinality=1,
    value_format='str',
    dependent_property_cardinality=0,
)
```

