---
atom_id: CA-R-2672
ref_id: CA-R-2672
role: Requirement
form: Scope Unit Declaration
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//WORKFLOWS
tier: 3
status: active
version: 2
updated_at: '2026-11-12T18:32:56.578538+00:00'
container:
  scope_unit: CA-SU-16
destination:
  file:
    name: CA-R-2672-TOOLS-SCOPE_UNIT_DECLARATION--declare-workflows.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/04_requirement
---
## Summary

Declare WORKFLOWS

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import ScopeUnit

declare_entity(
    entity_name='WORKFLOWS',
    instance=ScopeUnit(
        structural_level=4,
        id='CA-SU-33',
        name='WORKFLOWS',
        label='FEATURE_GROUP',
        ordered=False,
        container='TOOLS',
    ),
)
```

