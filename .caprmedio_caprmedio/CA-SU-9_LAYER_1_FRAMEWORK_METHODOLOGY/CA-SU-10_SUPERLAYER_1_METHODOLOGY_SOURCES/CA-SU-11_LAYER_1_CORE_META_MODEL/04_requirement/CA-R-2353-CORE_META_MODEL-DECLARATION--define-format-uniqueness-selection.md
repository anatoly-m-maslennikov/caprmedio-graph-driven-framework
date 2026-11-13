---
atom_id: CA-R-2353
ref_id: CA-R-2353
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Format.Uniqueness Selection
tier: 1
status: active
version: 7
updated_at: '2026-11-12T21:16:52.698794+00:00'
carrier_destination:
  file:
    name: CA-R-2353-CORE_META_MODEL-DECLARATION--define-format-uniqueness-selection.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Format Uniqueness Selection

## Claim

### Prose Claim


Format Uniqueness Selection identifies the comparison population for a
Property uniqueness check. It is optional and does not itself impose
uniqueness. It does not define a notation.



### Formal Claim

```python
from caprmedio.formal_claims import Cardinality, declare_entity

declare_entity(
    entity_name="Uniqueness Selection",
    relation_name="IS_PROPERTY_OF",
    base_path="Format",
    value_format=str,
    value_cardinality=Cardinality(minimum=0, maximum=1),
    dependent_property_cardinality=0,
)
```
