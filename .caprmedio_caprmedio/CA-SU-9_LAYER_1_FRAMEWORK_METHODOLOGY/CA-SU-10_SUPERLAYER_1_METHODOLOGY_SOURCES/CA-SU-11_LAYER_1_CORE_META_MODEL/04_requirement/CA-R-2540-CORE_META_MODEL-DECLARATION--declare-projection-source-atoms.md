---
atom_id: CA-R-2540
ref_id: CA-R-2540
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection.Source.Atoms
tier: 3
status: active
version: 3
updated_at: '2026-11-12T17:23:54+00:00'
carrier_destination:
  file:
    name: CA-R-2540-CORE_META_MODEL-DECLARATION--declare-projection-source-atoms.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare Projection.Source.Atoms

## Claim

### Prose Claim



Each value is an Atom ID with an explicit Version.
### Formal Claim

```python
# model
from caprmedio.formal_claims import Cardinality, declare_entity

declare_entity(
    entity_name='Atoms',
    relation_name='IS_PROPERTY_OF',
    base_path='Projection.Source',
    property_occurrence_cardinality=Cardinality(minimum=0, maximum=1),
    value_cardinality=Cardinality(minimum=0, maximum=None),
    value_format='str',
    dependent_property_cardinality=0,
)
```

