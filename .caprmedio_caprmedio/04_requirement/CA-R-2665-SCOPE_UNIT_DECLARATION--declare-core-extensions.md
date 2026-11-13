---
atom_id: CA-R-2665
ref_id: CA-R-2665
role: Requirement
form: Scope Unit Declaration
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//CORE_EXTENSIONS
tier: 3
status: active
version: 2
updated_at: '2026-11-12T18:36:47.434948+00:00'
container:
  scope_unit: CA-SU-00
destination:
  file:
    name: CA-R-2665-SCOPE_UNIT_DECLARATION--declare-core-extensions.md
    path: .caprmedio_caprmedio/04_requirement
---
## Summary

Declare CORE_EXTENSIONS

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import ScopeUnit

declare_entity(
    entity_name='CORE_EXTENSIONS',
    instance=ScopeUnit(
        structural_level=1,
        id='CA-SU-26',
        name='CORE_EXTENSIONS',
        label='LAYER',
        ordered=True,
        order_number=4,
        container='caprmedio',
    ),
)
```

