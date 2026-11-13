---
atom_id: CA-R-2669
ref_id: CA-R-2669
role: Requirement
form: Scope Unit Declaration
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//ADAPTERS
tier: 3
status: active
version: 2
updated_at: '2026-11-12T18:32:10.605286+00:00'
container:
  scope_unit: CA-SU-16
destination:
  file:
    name: CA-R-2669-TOOLS-SCOPE_UNIT_DECLARATION--declare-adapters.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/04_requirement
---
## Summary

Declare ADAPTERS

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import ScopeUnit

declare_entity(
    entity_name='ADAPTERS',
    instance=ScopeUnit(
        structural_level=4,
        id='CA-SU-30',
        name='ADAPTERS',
        label='FEATURE_GROUP',
        ordered=False,
        container='TOOLS',
    ),
)
```

