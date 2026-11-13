---
atom_id: CA-R-2681
ref_id: CA-R-2681
role: Requirement
form: Scope Unit Declaration
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//WORKFLOW_SCHEDULER
tier: 3
status: active
version: 2
updated_at: '2026-11-12T18:37:20.805017+00:00'
container:
  scope_unit: CA-SU-32
destination:
  file:
    name: CA-R-2681-SCHEDULERS-SCOPE_UNIT_DECLARATION--declare-workflow-scheduler.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/CA-SU-32_FEATURE_GROUP_SCHEDULERS/04_requirement
---
## Summary

Declare WORKFLOW_SCHEDULER

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import ScopeUnit

declare_entity(
    entity_name='WORKFLOW_SCHEDULER',
    instance=ScopeUnit(
        structural_level=5,
        id='CA-SU-42',
        name='WORKFLOW_SCHEDULER',
        label='FEATURE_GROUP',
        ordered=False,
        container='SCHEDULERS',
    ),
)
```

