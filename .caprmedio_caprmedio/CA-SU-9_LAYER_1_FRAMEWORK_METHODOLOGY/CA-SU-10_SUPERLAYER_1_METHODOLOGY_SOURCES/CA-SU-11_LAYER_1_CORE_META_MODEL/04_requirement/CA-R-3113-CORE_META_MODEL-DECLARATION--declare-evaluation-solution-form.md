---
identity:
  atom_id: CA-R-3113
  ref_id: CA-R-3113
context:
  role: requirement
  form: declaration
  container:
    scope_unit: CA-SU-11
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Evaluation)/(.Header.Context.Form
      := Solution)
  tier: 3
relations:
  is_replacement_for:
  - CA-R-3002
state:
  version: 1
  status: active
  updated_at: '2026-11-12T20:07:34.173138+00:00'
destination:
  file:
    name: CA-R-3113-CORE_META_MODEL-DECLARATION--declare-evaluation-solution-form.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---

## Summary

Declare Evaluation Solution Form

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import Evaluation

class Solution(Evaluation):
    pass

declare_entity(
    entity_class=Solution,
    entity_name='Solution',
    qualification_property_path='Atom.Header.Context.Form',
)
```

## Semantics

A Solution specifies the contribution that realizes a Scope Unit’s responsibility across the unit and its descendants. Its Role identifies the contribution.
