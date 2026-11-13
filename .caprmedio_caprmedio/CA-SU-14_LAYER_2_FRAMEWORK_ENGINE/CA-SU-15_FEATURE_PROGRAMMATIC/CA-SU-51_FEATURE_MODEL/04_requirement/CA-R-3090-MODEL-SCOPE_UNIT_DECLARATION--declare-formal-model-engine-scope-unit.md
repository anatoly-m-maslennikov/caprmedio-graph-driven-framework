---
identity:
  atom_id: CA-R-3090
  ref_id: CA-R-3090
context:
  role: requirement
  form: scope_unit_declaration
  tier: 3
  container:
    scope_unit: CA-SU-51
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//FORMAL_MODEL_ENGINE
state:
  version: 3
  status: active
  updated_at: '2026-11-13T15:14:02.576340+00:00'
destination:
  file:
    name: CA-R-3090-MODEL-SCOPE_UNIT_DECLARATION--declare-formal-model-engine-scope-unit.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-51_FEATURE_MODEL/04_requirement
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
        structural_level=4,
        label='FEATURE',
        ordered=False,
        container='MODEL',
    ),
)
```
