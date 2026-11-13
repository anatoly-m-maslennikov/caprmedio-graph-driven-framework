---
atom_id: CA-R-2629
ref_id: CA-R-2629
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings.RMED Review.Context Headroom Fraction
tier: 3
status: active
version: 3
updated_at: '2026-11-12T19:06:43.021656+00:00'
carrier_destination:
  file:
    name: CA-R-2629-CORE_META_MODEL-DECLARATION--declare-project-settings-rmed-review-context-headroom-fraction.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---

## Summary

Declare Project.Settings.RMED Review.Context Headroom Fraction

## Claim

### Prose Claim


When present, the value is finite and strictly between zero and one.

### Formal Claim

```python
from caprmedio.formal_claims import Cardinality, declare_entity

declare_entity(
    entity_name="Context Headroom Fraction",
    relation_name="IS_PROPERTY_OF",
    base_path="Project.Settings.RMED Review",
    value_format=float,
    value_cardinality=Cardinality(minimum=0, maximum=1),
    dependent_property_cardinality=0,
)
```

