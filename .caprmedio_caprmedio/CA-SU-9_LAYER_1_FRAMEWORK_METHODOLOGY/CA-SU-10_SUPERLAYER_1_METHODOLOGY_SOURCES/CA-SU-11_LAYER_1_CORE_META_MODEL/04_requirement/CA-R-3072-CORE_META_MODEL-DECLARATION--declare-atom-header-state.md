---
identity:
  id: CA-R-3072
  ref_id: CA-R-3072
context:
  container:
    scope_unit: CA-SU-11
  role: requirement
  form: declaration
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom.Header.State
  tier: 3
state:
  status: active
  version: 2
  updated_at: '2026-11-13T00:27:04.807824+00:00'
destination:
  file:
    name: CA-R-3072-CORE_META_MODEL-DECLARATION--declare-atom-header-state.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---


## Summary

Declare Atom.Header.State

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity

declare_entity(
    entity_name='State',
    relation_name="IS_PROPERTY_OF",
    base_path="Atom.Header",
    property_occurrence_cardinality=1,
    value_cardinality=0,
    dependent_property_cardinality=3,
    allowed_dependent_property_names=('Status', 'Version', 'Updated At'),
    ordered_dependent_property_pairs=(('Status', 'Version'), ('Version', 'Updated At')),
)
```
