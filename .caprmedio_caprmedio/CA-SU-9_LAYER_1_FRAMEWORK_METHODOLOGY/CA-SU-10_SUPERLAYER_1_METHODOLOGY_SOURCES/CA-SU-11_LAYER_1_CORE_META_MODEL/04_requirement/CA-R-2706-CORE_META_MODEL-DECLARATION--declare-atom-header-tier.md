---
atom_id: CA-R-2706
ref_id: CA-R-2706
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Context.Tier
tier: 3
status: active
version: 3
updated_at: '2026-11-12T19:06:44.073009+00:00'
carrier_destination:
  file:
    name: CA-R-2706-CORE_META_MODEL-DECLARATION--declare-atom-header-tier.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare Atom.Header.Tier

## Claim

### Prose Claim

Atom.Header.Tier stores one integer value and an optional Tier Label; the Formal Claim defines their representation.

### Formal Claim

```python
from caprmedio.formal_claims import Cardinality, declare_entity

declare_entity(
    entity_name="Tier",
    relation_name="IS_PROPERTY_OF",
    base_path="Atom.Header.Context",
    property_occurrence_cardinality=1,
    value_format=int,
    value_cardinality=1,
    dependent_property_cardinality=Cardinality(minimum=0, maximum=1),
    allowed_dependent_property_names=("Label",),
    minimum_value=-1,
)
```
