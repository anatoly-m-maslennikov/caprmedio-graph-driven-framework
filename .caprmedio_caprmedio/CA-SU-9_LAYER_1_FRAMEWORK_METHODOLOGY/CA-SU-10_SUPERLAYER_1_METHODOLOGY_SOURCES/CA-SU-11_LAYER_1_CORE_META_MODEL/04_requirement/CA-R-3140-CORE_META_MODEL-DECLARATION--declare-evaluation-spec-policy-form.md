---
identity:
  atom_id: CA-R-3140
  ref_id: CA-R-3140
context:
  role: requirement
  form: declaration
  container:
    scope_unit: CA-SU-11
  tier: 3
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Evaluation)/(.Header.Context.Form
      := Spec Policy)
relations:
  IS_REPLACEMENT_FOR:
  - CA-R-3123
state:
  version: 1
  status: active
  updated_at: '2026-11-13T15:39:40.855648+00:00'
destination:
  file:
    name: CA-R-3140-CORE_META_MODEL-DECLARATION--declare-evaluation-spec-policy-form.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare Evaluation Spec Policy Form

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import Evaluation

class SpecPolicy(Evaluation):
    pass

declare_entity(
    entity_class=SpecPolicy,
    entity_name='Spec Policy',
    qualification_property_path='Atom.Header.Context.Form',
)
```

## Semantics

A Spec Policy governs how to write and review Atoms of the same Role whose main subject is its own main subject or a descendant.