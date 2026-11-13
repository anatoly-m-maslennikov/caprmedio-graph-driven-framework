---
atom_id: CA-R-2702
ref_id: CA-R-2702
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Context.Role
tier: 3
status: active
version: 3
updated_at: '2026-11-12T17:23:54+00:00'
carrier_destination:
  file:
    name: CA-R-2702-CORE_META_MODEL-DECLARATION--declare-atom-header-role.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare Atom.Header.Role

## Claim


### Prose Claim

Role Order Number classifies the Role-qualified Atom kind in the Model. Each Role Declaration assigns exactly one positive integer. Order numbers are distinct across Roles. Gaps are allowed.

### Formal Claim

```python
# model
from caprmedio.formal_claims import declare_entity

declare_entity(
    entity_name='Role',
    relation_name='IS_PROPERTY_OF',
    base_path='Atom.Header.Context',
    property_occurrence_cardinality=1,
    value_cardinality=1,
    value_format='str',
    dependent_property_cardinality=0,
)
```
