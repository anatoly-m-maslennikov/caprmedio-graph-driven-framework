---
identity:
  atom_id: CA-R-3130
  ref_id: CA-R-3130
context:
  role: requirement
  form: declaration
  container:
    scope_unit: CA-SU-11
  tier: 3
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Scope Unit.Paths.Delivery
state:
  version: 1
  status: active
  updated_at: '2026-11-12T22:04:06.649489+00:00'
destination:
  file:
    name: CA-R-3130-CORE_META_MODEL-DECLARATION--declare-scope-unit-delivery-path.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare Scope Unit Delivery Path

## Claim

### Prose Claim

Delivery is the Project-root-relative path to the Scope Unit’s delivery folder. Use the actual folder names.

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity

declare_entity(
    entity_name="Delivery",
    relation_name="IS_PROPERTY_OF",
    base_path="Scope Unit.Paths",
    property_occurrence_cardinality=1,
    value_format=str,
    value_cardinality=1,
    dependent_property_cardinality=0,
)
```
