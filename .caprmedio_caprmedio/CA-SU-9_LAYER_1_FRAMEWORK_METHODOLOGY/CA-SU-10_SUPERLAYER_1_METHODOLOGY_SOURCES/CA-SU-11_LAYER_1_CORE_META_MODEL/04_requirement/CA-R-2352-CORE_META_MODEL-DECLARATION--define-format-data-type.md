---
atom_id: CA-R-2352
ref_id: CA-R-2352
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Format.Data Type
tier: 1
status: active
version: 6
updated_at: '2026-11-12T21:16:49.823331+00:00'
carrier_destination:
  file:
    name: CA-R-2352-CORE_META_MODEL-DECLARATION--define-format-data-type.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Format Data Type

## Claim

### Prose Claim


Format Data Type names the admissible value domain of a direct Property value.
It is separate from cardinality. The initial vocabulary is provisional; list,
map and reference semantics remain with the governing Format definition.



### Formal Claim

```python
from caprmedio.formal_claims import declare_entity

declare_entity(
    entity_name="Data Type",
    relation_name="IS_PROPERTY_OF",
    base_path="Format",
    property_occurrence_cardinality=1,
    value_format=str,
    value_cardinality=1,
    dependent_property_cardinality=0,
)
```
