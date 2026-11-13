---
identity:
  atom_id: CA-R-3099
  ref_id: CA-R-3099
context:
  role: requirement
  form: scope_unit_declaration
  container:
    scope_unit: CA-SU-00
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//FRAMEWORK_ENGINE
  tier: 3
state:
  version: 1
  status: active
  updated_at: '2026-11-12T19:26:40.422899+00:00'
destination:
  file:
    name: CA-R-3099-SCOPE_UNIT_DECLARATION--declare-framework-engine.md
    path: .caprmedio_caprmedio/04_requirement
---
## Summary

Declare FRAMEWORK_ENGINE

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import ScopeUnit

declare_entity(
    entity_name='FRAMEWORK_ENGINE',
    instance=ScopeUnit(
        id='CA-SU-14',
        name='FRAMEWORK_ENGINE',
        label='LAYER',
        ordered=True,
        order_number=2,
        container='caprmedio',
        structural_level=1,
    ),
)
```
