---
identity:
  atom_id: CA-R-3087
  ref_id: CA-R-3087
context:
  role: requirement
  form: declaration
  container:
    scope_unit: CA-SU-11
  tier: 3
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/(.Header.Context.Form
      := Decision)
state:
  version: 1
  status: active
  updated_at: '2026-11-12T12:33:04.158402+00:00'
destination:
  file:
    name: CA-R-3087-CORE_META_MODEL-DECLARATION--declare-operations-decision-form.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
relations:
  IS_REPLACEMENT_FOR:
  - CA-R-3005
---

## Summary

Declare Operations Decision Form

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import Operations

class Decision(Operations):
    pass

declare_entity(
    entity_class=Decision,
    entity_name='Decision',
    qualification_property_path='Atom.Header.Context.Form',
)
```

## Semantics

A Decision records a particular local choice. Applicable governing constraints continue to apply.
