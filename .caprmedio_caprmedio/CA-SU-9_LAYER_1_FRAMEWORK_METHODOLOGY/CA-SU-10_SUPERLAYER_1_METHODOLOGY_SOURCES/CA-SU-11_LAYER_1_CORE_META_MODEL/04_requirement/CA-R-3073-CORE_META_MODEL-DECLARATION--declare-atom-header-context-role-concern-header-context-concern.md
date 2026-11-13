---
identity:
  id: CA-R-3073
  ref_id: CA-R-3073
context:
  container:
    scope_unit: CA-SU-11
  role: requirement
  form: declaration
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Concern).Header.Context.Concern
  tier: 3
state:
  status: active
  version: 2
  updated_at: '2026-11-12T19:20:12.374663+00:00'
destination:
  file:
    name: CA-R-3073-CORE_META_MODEL-DECLARATION--declare-atom-header-context-role-concern-header-context-concern.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---

## Summary

Declare Atom/(.Header.Context.Role := Concern).Header.Context.Concern

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import Concern

declare_entity(
    entity_name='Concern',
    relation_name="IS_PROPERTY_OF",
    base_path='Atom.Header.Context',
    property_occurrence_cardinality=1,
    value_cardinality=0,
    dependent_property_cardinality=1,
    allowed_dependent_property_names=('Priority',),
    applies_to_entity_classes=(Concern,),
)
```
