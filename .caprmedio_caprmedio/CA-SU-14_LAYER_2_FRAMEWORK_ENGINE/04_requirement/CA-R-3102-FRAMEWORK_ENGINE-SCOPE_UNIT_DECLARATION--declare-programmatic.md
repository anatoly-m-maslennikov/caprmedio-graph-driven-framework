---
identity:
  atom_id: CA-R-3102
  ref_id: CA-R-3102
context:
  role: requirement
  form: scope_unit_declaration
  container:
    scope_unit: CA-SU-14
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//PROGRAMMATIC
  tier: 3
state:
  version: 1
  status: active
  updated_at: '2026-11-12T19:26:52.515731+00:00'
destination:
  file:
    name: CA-R-3102-FRAMEWORK_ENGINE-SCOPE_UNIT_DECLARATION--declare-programmatic.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/04_requirement
---
## Summary

Declare PROGRAMMATIC

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import ScopeUnit

declare_entity(
    entity_name='PROGRAMMATIC',
    instance=ScopeUnit(
        id='CA-SU-15',
        name='PROGRAMMATIC',
        label='FEATURE',
        ordered=False,
        container='FRAMEWORK_ENGINE',
        structural_level=2,
    ),
)
```
