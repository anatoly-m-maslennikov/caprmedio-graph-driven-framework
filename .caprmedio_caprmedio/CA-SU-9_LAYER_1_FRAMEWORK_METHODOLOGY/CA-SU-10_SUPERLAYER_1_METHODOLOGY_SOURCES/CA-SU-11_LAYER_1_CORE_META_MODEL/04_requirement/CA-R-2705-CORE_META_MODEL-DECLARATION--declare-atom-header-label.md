---
atom_id: CA-R-2705
ref_id: CA-R-2705
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Context.Label
tier: 3
status: active
version: 5
updated_at: '2026-11-13T03:26:58.057112+00:00'
carrier_destination:
  file:
    name: CA-R-2705-CORE_META_MODEL-DECLARATION--declare-atom-header-label.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare Atom.Header.Label

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import Cardinality, declare_entity

declare_entity(
    entity_name="Label",
    relation_name="IS_PROPERTY_OF",
    base_path="Atom.Header.Context",
    value_format=str,
    value_cardinality=Cardinality(minimum=0, maximum=1),
    dependent_property_cardinality=0,
    fallback_property_name="Form",
)
```
