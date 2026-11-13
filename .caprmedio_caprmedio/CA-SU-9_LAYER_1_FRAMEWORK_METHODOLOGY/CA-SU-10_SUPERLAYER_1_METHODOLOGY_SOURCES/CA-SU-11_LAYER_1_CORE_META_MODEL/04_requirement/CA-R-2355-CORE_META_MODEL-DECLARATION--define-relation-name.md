---
atom_id: CA-R-2355
ref_id: CA-R-2355
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation.Name
tier: 1
status: active
version: 8
updated_at: '2026-11-12T21:29:37.101539+00:00'
carrier_destination:
  file:
    name: CA-R-2355-CORE_META_MODEL-DECLARATION--define-relation-name.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Define Relation Name

## Claim

### Prose Claim


Relation Name is the canonical name of a reusable Relation Type.
### Formal Claim

```python
from caprmedio.formal_claims import declare_entity

declare_entity(
    entity_name="Name",
    relation_name="IS_PROPERTY_OF",
    base_path="Relation",
    property_occurrence_cardinality=1,
    value_format=str,
    value_cardinality=1,
    dependent_property_cardinality=0,
)
```
