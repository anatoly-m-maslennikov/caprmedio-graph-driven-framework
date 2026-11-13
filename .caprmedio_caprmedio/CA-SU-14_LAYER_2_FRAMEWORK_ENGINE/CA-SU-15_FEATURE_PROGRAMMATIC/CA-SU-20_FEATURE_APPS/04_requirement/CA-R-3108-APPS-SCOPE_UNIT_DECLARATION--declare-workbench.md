---
identity:
  atom_id: CA-R-3108
  ref_id: CA-R-3108
context:
  role: requirement
  form: scope_unit_declaration
  container:
    scope_unit: CA-SU-20
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//WORKBENCH
  tier: 3
state:
  version: 1
  status: active
  updated_at: '2026-11-12T19:27:09.922481+00:00'
destination:
  file:
    name: CA-R-3108-APPS-SCOPE_UNIT_DECLARATION--declare-workbench.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/04_requirement
---
## Summary

Declare WORKBENCH

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import ScopeUnit

declare_entity(
    entity_name='WORKBENCH',
    instance=ScopeUnit(
        id='CA-SU-43',
        name='WORKBENCH',
        label='APP',
        ordered=False,
        container='APPS',
        structural_level=4,
    ),
)
```
