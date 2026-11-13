---
atom_id: CA-R-2651
ref_id: CA-R-2651
role: Requirement
form: Scope Unit Declaration
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//INSTALLED_EXTENSIONS
tier: 3
status: active
version: 2
updated_at: '2026-11-12T18:36:50.530980+00:00'
container:
  scope_unit: CA-SU-10
destination:
  file:
    name: CA-R-2651-METHODOLOGY_SOURCES-SCOPE_UNIT_DECLARATION--declare-installed-extensions.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/04_requirement
---
## Summary

Declare INSTALLED_EXTENSIONS

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import ScopeUnit

declare_entity(
    entity_name='INSTALLED_EXTENSIONS',
    instance=ScopeUnit(
        structural_level=3,
        id='CA-SU-12',
        name='INSTALLED_EXTENSIONS',
        label='LAYER',
        ordered=True,
        order_number=2,
        container='METHODOLOGY_SOURCES',
    ),
)
```

