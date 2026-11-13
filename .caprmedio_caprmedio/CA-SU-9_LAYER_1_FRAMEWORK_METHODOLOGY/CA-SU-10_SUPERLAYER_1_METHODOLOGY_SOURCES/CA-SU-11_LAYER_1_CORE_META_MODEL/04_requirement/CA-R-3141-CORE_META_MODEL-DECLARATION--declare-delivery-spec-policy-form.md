---
identity:
  atom_id: CA-R-3141
  ref_id: CA-R-3141
context:
  role: requirement
  form: declaration
  container:
    scope_unit: CA-SU-11
  tier: 3
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Delivery)/(.Header.Context.Form
      := Spec Policy)
relations:
  IS_REPLACEMENT_FOR:
  - CA-R-3124
state:
  version: 1
  status: active
  updated_at: '2026-11-13T15:39:45.397206+00:00'
destination:
  file:
    name: CA-R-3141-CORE_META_MODEL-DECLARATION--declare-delivery-spec-policy-form.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare Delivery Spec Policy Form

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import Delivery

class SpecPolicy(Delivery):
    pass

declare_entity(
    entity_class=SpecPolicy,
    entity_name='Spec Policy',
    qualification_property_path='Atom.Header.Context.Form',
)
```

## Semantics

A Spec Policy governs how to write and review Atoms of the same Role whose main subject is its own main subject or a descendant.