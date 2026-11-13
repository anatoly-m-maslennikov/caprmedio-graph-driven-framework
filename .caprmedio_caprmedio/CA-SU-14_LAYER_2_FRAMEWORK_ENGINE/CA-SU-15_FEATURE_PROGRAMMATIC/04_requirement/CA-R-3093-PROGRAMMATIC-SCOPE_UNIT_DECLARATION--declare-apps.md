---
identity:
  atom_id: CA-R-3093
  ref_id: CA-R-3093
context:
  role: requirement
  form: scope_unit_declaration
  container:
    scope_unit: CA-SU-15
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//APPS
  tier: 3
state:
  version: 1
  status: active
  updated_at: '2026-11-12T19:26:22.245524+00:00'
destination:
  file:
    name: CA-R-3093-PROGRAMMATIC-SCOPE_UNIT_DECLARATION--declare-apps.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement
---
## Summary

Declare APPS

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import ScopeUnit

declare_entity(
    entity_name='APPS',
    instance=ScopeUnit(
        id='CA-SU-20',
        name='APPS',
        label='FEATURE',
        ordered=False,
        container='PROGRAMMATIC',
        structural_level=3,
    ),
)
```
