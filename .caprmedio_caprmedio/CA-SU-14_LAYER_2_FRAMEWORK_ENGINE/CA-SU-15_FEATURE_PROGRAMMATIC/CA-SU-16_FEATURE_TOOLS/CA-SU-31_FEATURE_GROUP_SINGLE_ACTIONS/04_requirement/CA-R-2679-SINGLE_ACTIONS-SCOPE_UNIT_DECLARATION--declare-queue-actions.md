---
atom_id: CA-R-2679
ref_id: CA-R-2679
role: Requirement
form: Scope Unit Declaration
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//QUEUE_ACTIONS
tier: 3
status: active
version: 2
updated_at: '2026-11-12T18:37:11.275676+00:00'
container:
  scope_unit: CA-SU-31
destination:
  file:
    name: CA-R-2679-SINGLE_ACTIONS-SCOPE_UNIT_DECLARATION--declare-queue-actions.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/CA-SU-31_FEATURE_GROUP_SINGLE_ACTIONS/04_requirement
---
## Summary

Declare QUEUE_ACTIONS

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import ScopeUnit

declare_entity(
    entity_name='QUEUE_ACTIONS',
    instance=ScopeUnit(
        structural_level=5,
        id='CA-SU-40',
        name='QUEUE_ACTIONS',
        label='FEATURE_GROUP',
        ordered=False,
        container='SINGLE_ACTIONS',
    ),
)
```

