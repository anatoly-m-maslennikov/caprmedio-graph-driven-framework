---
identity:
  atom_id: CA-R-3090
  ref_id: CA-R-3090@2
context:
  role: requirement
  form: scope_unit_declaration
  tier: 3
  container:
    scope_unit: CA-SU-15
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//FORMAL_MODEL_ENGINE
state:
  version: 2
  status: archived
  updated_at: '2026-11-12T18:25:04.925507+00:00'
destination:
  file:
    name: CA-R-3090@2-PROGRAMMATIC-SCOPE_UNIT_DECLARATION--declare-formal-model-engine-scope-unit.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement/099_archived
---
## Summary

Declare FORMAL MODEL ENGINE Scope Unit

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import ScopeUnit

declare_entity(
    entity_name='FORMAL_MODEL_ENGINE',
    instance=ScopeUnit(
        id='CA-SU-50',
        name='FORMAL_MODEL_ENGINE',
        structural_level=3,
        label='FEATURE',
        ordered=False,
        container='PROGRAMMATIC',
    ),
)
```
