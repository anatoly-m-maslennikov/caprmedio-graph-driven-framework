---
identity:
  atom_id: CA-R-3109
  ref_id: CA-R-3109
context:
  role: requirement
  form: scope_unit_declaration
  container:
    scope_unit: CA-SU-43
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//WORKBENCH_BACKEND
  tier: 3
state:
  version: 1
  status: active
  updated_at: '2026-11-12T19:27:12.060587+00:00'
destination:
  file:
    name: CA-R-3109-WORKBENCH-SCOPE_UNIT_DECLARATION--declare-workbench-backend.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement
---
## Summary

Declare WORKBENCH_BACKEND

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import ScopeUnit

declare_entity(
    entity_name='WORKBENCH_BACKEND',
    instance=ScopeUnit(
        id='CA-SU-45',
        name='WORKBENCH_BACKEND',
        label='FEATURE',
        ordered=False,
        container='WORKBENCH',
        structural_level=5,
    ),
)
```
