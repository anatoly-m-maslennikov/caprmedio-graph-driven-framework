---
identity:
  atom_id: CA-R-3098
  ref_id: CA-R-3098
context:
  role: requirement
  form: scope_unit_declaration
  container:
    scope_unit: CA-SU-00
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//FRAMEWORK_DELIVERY
  tier: 3
state:
  version: 1
  status: active
  updated_at: '2026-11-12T19:26:37.054388+00:00'
destination:
  file:
    name: CA-R-3098-SCOPE_UNIT_DECLARATION--declare-framework-delivery.md
    path: .caprmedio_caprmedio/04_requirement
---
## Summary

Declare FRAMEWORK_DELIVERY

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import ScopeUnit

declare_entity(
    entity_name='FRAMEWORK_DELIVERY',
    instance=ScopeUnit(
        id='CA-SU-27',
        name='FRAMEWORK_DELIVERY',
        label='LAYER',
        ordered=True,
        order_number=5,
        container='caprmedio',
        structural_level=1,
    ),
)
```
