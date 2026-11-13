---
identity:
  atom_id: CA-R-3116
  ref_id: CA-R-3116@1
context:
  role: requirement
  form: declaration
  container:
    scope_unit: CA-SU-11
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Requirement)/(.Header.Context.Form
      := Direct Policy)
  tier: 3
relations:
  is_replacement_for:
  - CA-R-3003
state:
  version: 1
  status: archived
  updated_at: '2026-11-12T20:07:45.645838+00:00'
destination:
  file:
    name: CA-R-3116@1-CORE_META_MODEL-DECLARATION--declare-requirement-direct-policy-form.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
---

## Summary

Declare Requirement Direct Policy Form

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import Requirement

class DirectPolicy(Requirement):
    pass

declare_entity(
    entity_class=DirectPolicy,
    entity_name='Direct Policy',
    qualification_property_path='Atom.Header.Context.Form',
)
```

## Semantics

A Direct Policy applies to all descendants recursively without a local copy. A genuine SPECIALIZES Atom may add applicable detail while preserving parent constraints.
