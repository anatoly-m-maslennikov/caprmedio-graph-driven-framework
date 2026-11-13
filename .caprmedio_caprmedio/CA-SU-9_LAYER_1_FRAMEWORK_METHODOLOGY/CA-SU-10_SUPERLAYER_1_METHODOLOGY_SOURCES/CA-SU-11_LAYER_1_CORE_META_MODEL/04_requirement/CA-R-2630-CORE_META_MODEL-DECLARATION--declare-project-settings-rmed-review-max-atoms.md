---
atom_id: CA-R-2630
ref_id: CA-R-2630
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings.RMED Review.Max Atoms
tier: 3
status: active
version: 3
updated_at: '2026-11-12T17:23:54+00:00'
carrier_destination:
  file:
    name: CA-R-2630-CORE_META_MODEL-DECLARATION--declare-project-settings-rmed-review-max-atoms.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---

## Summary

Declare Project.Settings.RMED Review.Max Atoms

## Claim

### Prose Claim


When present, the value is positive. Its absence supplies no default.

### Formal Claim

```python
# model
from caprmedio.formal_claims import Cardinality, declare_entity

declare_entity(
    entity_name='Max Atoms',
    relation_name='IS_PROPERTY_OF',
    base_path='Project.Settings.RMED Review',
    value_cardinality=Cardinality(minimum=0, maximum=1),
    value_format='int',
    dependent_property_cardinality=0,
)
```

