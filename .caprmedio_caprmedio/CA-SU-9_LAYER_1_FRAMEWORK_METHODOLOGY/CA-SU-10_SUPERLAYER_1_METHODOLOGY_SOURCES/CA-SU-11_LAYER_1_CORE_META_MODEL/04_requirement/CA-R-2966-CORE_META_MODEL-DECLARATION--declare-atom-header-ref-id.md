---
atom_id: CA-R-2966
ref_id: CA-R-2966
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Identity.Ref ID
tier: 3
status: active
version: 3
updated_at: '2026-11-12T17:23:54+00:00'
carrier_destination:
  file:
    name: CA-R-2966-CORE_META_MODEL-DECLARATION--declare-atom-header-ref-id.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare Atom.Header.Ref ID

## Claim

### Prose Claim

For an Atom in the Current or Backlog Status Group, Ref ID is its base Atom ID. For an Archived Atom, Ref ID is `<ID>@<Version>`. For a Draft Atom, Ref ID is `<ID>@<Version>-draft`.

### Formal Claim

```python
# model
from caprmedio.formal_claims import declare_entity

declare_entity(
    entity_name='Ref ID',
    relation_name='IS_PROPERTY_OF',
    base_path='Atom.Header.Identity',
    property_occurrence_cardinality=1,
    value_cardinality=1,
    value_format='str',
    dependent_property_cardinality=0,
)
```
