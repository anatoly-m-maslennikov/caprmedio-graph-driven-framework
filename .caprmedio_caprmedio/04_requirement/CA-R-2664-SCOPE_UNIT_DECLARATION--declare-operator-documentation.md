---
atom_id: CA-R-2664
ref_id: CA-R-2664
role: Requirement
form: Scope Unit Declaration
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//OPERATOR_DOCUMENTATION
tier: 3
status: active
version: 2
updated_at: '2026-11-12T18:36:59.009278+00:00'
container:
  scope_unit: CA-SU-00
destination:
  file:
    name: CA-R-2664-SCOPE_UNIT_DECLARATION--declare-operator-documentation.md
    path: .caprmedio_caprmedio/04_requirement
---
## Summary

Declare OPERATOR_DOCUMENTATION

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import ScopeUnit

declare_entity(
    entity_name='OPERATOR_DOCUMENTATION',
    instance=ScopeUnit(
        structural_level=1,
        id='CA-SU-25',
        name='OPERATOR_DOCUMENTATION',
        label='LAYER',
        ordered=True,
        order_number=3,
        container='caprmedio',
    ),
)
```

