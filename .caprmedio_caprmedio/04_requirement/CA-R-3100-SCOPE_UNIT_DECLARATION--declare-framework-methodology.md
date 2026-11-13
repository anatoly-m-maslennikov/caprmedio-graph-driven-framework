---
identity:
  atom_id: CA-R-3100
  ref_id: CA-R-3100
context:
  role: requirement
  form: scope_unit_declaration
  container:
    scope_unit: CA-SU-00
  topics:
    main_subject: scope_unit//FRAMEWORK_METHODOLOGY
  tier: 3
state:
  version: 1
  status: active
  updated_at: '2026-11-12T19:26:43.187570+00:00'
destination:
  file:
    name: CA-R-3100-SCOPE_UNIT_DECLARATION--declare-framework-methodology.md
    path: .caprmedio_caprmedio/04_requirement
---
## Summary

Declare FRAMEWORK_METHODOLOGY

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import ScopeUnit

declare_entity(
    entity_name='FRAMEWORK_METHODOLOGY',
    instance=ScopeUnit(
        id='CA-SU-9',
        name='FRAMEWORK_METHODOLOGY',
        label='LAYER',
        ordered=True,
        order_number=1,
        container='caprmedio',
        structural_level=1,
    ),
)
```
