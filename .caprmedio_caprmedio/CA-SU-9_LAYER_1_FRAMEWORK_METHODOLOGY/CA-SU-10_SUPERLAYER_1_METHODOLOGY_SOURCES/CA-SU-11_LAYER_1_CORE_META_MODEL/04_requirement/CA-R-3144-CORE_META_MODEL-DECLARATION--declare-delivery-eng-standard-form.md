---
identity:
  atom_id: CA-R-3144
  ref_id: CA-R-3144
context:
  role: requirement
  form: declaration
  container:
    scope_unit: CA-SU-11
  tier: 3
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Delivery)/(.Header.Context.Form
      := Eng Standard)
relations:
  IS_REPLACEMENT_FOR:
  - CA-R-3119
state:
  version: 1
  status: active
  updated_at: '2026-11-13T15:40:01.174594+00:00'
destination:
  file:
    name: CA-R-3144-CORE_META_MODEL-DECLARATION--declare-delivery-eng-standard-form.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare Delivery Eng Standard Form

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import Delivery

class EngStandard(Delivery):
    pass

declare_entity(
    entity_class=EngStandard,
    entity_name='Eng Standard',
    qualification_property_path='Atom.Header.Context.Form',
)
```

## Semantics

An Eng Standard applies directly to implementation within its owning Scope Unit and descendant Scope Units where its Claim applies.