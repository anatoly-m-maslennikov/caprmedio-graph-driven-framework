---
atom_id: CA-R-2717
ref_id: CA-R-2717
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Destination.File.Name
tier: 3
status: active
version: 4
updated_at: '2026-11-12T17:23:54+00:00'
carrier_destination:
  file:
    name: CA-R-2717-CORE_META_MODEL-DECLARATION--declare-atom-header-carrier-destination-file-name.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare Atom.Header.Carrier Destination.File.Name

## Claim

### Prose Claim




Calculated full filename, including its extension.
### Formal Claim

```python
# model
from caprmedio.formal_claims import declare_entity

declare_entity(
    entity_name='Name',
    relation_name='IS_PROPERTY_OF',
    base_path='Atom.Header.Destination.File',
    value_cardinality=1,
    dependent_property_cardinality=0,
)
```

