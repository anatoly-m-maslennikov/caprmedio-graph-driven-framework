---
atom_id: CA-R-2503
ref_id: CA-R-2503
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Content.Details
tier: 3
status: active
version: 6
updated_at: '2026-11-12T12:33:04.158402+00:00'
carrier_destination:
  file:
    name: CA-R-2503-CORE_META_MODEL-DECLARATION--declare-atom-content-details.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare Atom.Content.Details

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import Cardinality, declare_entity
from caprmedio.model import Delivery, Evaluation, Method, Requirement

declare_entity(
    entity_name='Details',
    relation_name='IS_PROPERTY_OF',
    base_path='Atom.Content',
    value_cardinality=Cardinality(minimum=0, maximum=1),
    dependent_property_cardinality=Cardinality(minimum=0, maximum=None),
    dependent_property_name_format=str,
    applies_to_entity_classes=(Requirement, Method, Evaluation, Delivery),
)
```

