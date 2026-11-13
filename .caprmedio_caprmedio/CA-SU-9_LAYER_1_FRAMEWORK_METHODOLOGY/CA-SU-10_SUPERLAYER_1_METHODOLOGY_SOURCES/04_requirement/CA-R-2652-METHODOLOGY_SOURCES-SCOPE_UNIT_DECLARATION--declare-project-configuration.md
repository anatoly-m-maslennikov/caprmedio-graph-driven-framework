---
atom_id: CA-R-2652
ref_id: CA-R-2652
role: Requirement
form: Scope Unit Declaration
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
tier: 3
status: active
version: 2
updated_at: '2026-11-12T18:37:07.869068+00:00'
container:
  scope_unit: CA-SU-10
destination:
  file:
    name: CA-R-2652-METHODOLOGY_SOURCES-SCOPE_UNIT_DECLARATION--declare-project-configuration.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/04_requirement
---
## Summary

Declare PROJECT_CONFIGURATION

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import ScopeUnit

declare_entity(
    entity_name='PROJECT_CONFIGURATION',
    instance=ScopeUnit(
        structural_level=3,
        id='CA-SU-13',
        name='PROJECT_CONFIGURATION',
        label='LAYER',
        ordered=True,
        order_number=3,
        container='METHODOLOGY_SOURCES',
    ),
)
```

