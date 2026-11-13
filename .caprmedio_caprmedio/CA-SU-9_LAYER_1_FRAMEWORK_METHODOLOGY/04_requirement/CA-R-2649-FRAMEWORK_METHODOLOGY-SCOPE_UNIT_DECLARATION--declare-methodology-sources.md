---
atom_id: CA-R-2649
ref_id: CA-R-2649
role: Requirement
form: Scope Unit Declaration
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//METHODOLOGY_SOURCES
tier: 3
status: active
version: 2
updated_at: '2026-11-12T18:36:55.940001+00:00'
container:
  scope_unit: CA-SU-9
destination:
  file:
    name: CA-R-2649-FRAMEWORK_METHODOLOGY-SCOPE_UNIT_DECLARATION--declare-methodology-sources.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/04_requirement
---
## Summary

Declare METHODOLOGY_SOURCES

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import ScopeUnit

declare_entity(
    entity_name='METHODOLOGY_SOURCES',
    instance=ScopeUnit(
        structural_level=2,
        id='CA-SU-10',
        name='METHODOLOGY_SOURCES',
        label='SUPERLAYER',
        ordered=True,
        order_number=1,
        container='FRAMEWORK_METHODOLOGY',
    ),
)
```

