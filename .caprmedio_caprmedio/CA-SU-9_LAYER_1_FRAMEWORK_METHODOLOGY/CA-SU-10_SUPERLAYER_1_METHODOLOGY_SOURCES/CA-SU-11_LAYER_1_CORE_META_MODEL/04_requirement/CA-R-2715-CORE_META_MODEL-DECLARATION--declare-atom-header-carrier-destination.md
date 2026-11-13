---
atom_id: CA-R-2715
ref_id: CA-R-2715
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Destination
tier: 3
status: active
version: 2
updated_at: '2026-11-12T12:33:04.158402+00:00'
carrier_destination:
  file:
    name: CA-R-2715-CORE_META_MODEL-DECLARATION--declare-atom-header-carrier-destination.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare Atom.Header.Carrier Destination

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity

declare_entity(
    entity_name='Destination',
    relation_name='IS_PROPERTY_OF',
    base_path='Atom.Header',
    property_occurrence_cardinality=1,
    value_cardinality=0,
    dependent_property_cardinality=1,
    allowed_dependent_property_names=('File',),
)
```
