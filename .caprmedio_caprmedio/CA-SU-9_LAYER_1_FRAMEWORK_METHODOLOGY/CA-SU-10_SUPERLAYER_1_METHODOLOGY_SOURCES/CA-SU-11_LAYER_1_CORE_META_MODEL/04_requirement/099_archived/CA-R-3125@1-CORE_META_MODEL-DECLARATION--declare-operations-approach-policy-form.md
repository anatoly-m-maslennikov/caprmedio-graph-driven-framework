---
identity:
  atom_id: CA-R-3125
  ref_id: CA-R-3125@1
context:
  role: requirement
  form: declaration
  container:
    scope_unit: CA-SU-11
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/(.Header.Context.Form
      := Approach Policy)
  tier: 3
relations:
  is_replacement_for:
  - CA-R-3004
state:
  version: 1
  status: archived
  updated_at: '2026-11-12T20:08:14.879431+00:00'
destination:
  file:
    name: CA-R-3125@1-CORE_META_MODEL-DECLARATION--declare-operations-approach-policy-form.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
---

## Summary

Declare Operations Approach Policy Form

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import Operations

class ApproachPolicy(Operations):
    pass

declare_entity(
    entity_class=ApproachPolicy,
    entity_name='Approach Policy',
    qualification_property_path='Atom.Header.Context.Form',
)
```

## Semantics

An Approach Policy is conditional on its stated case. At every descendant where that case applies, a local Atom must bind the Policy to the actual case through SPECIALIZES. A reference alone is insufficient; the binding preserves parent constraints.
