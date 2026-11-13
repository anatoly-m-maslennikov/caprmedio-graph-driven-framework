---
identity:
  atom_id: CA-R-3103
  ref_id: CA-R-3103
context:
  role: requirement
  form: scope_unit_declaration
  container:
    scope_unit: CA-SU-15
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_TOOLS
  tier: 3
state:
  version: 1
  status: active
  updated_at: '2026-11-12T19:26:56.597822+00:00'
destination:
  file:
    name: CA-R-3103-PROGRAMMATIC-SCOPE_UNIT_DECLARATION--declare-project-tools.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement
---
## Summary

Declare PROJECT_TOOLS

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import ScopeUnit

declare_entity(
    entity_name='PROJECT_TOOLS',
    instance=ScopeUnit(
        id='CA-SU-19',
        name='PROJECT_TOOLS',
        label='FEATURE',
        ordered=False,
        container='PROGRAMMATIC',
        structural_level=3,
    ),
)
```
