---
identity:
  atom_id: CA-R-3105
  ref_id: CA-R-3105
context:
  role: requirement
  form: scope_unit_declaration
  container:
    scope_unit: CA-SU-22
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//SKILLS
  tier: 3
state:
  version: 1
  status: active
  updated_at: '2026-11-12T19:27:03.008803+00:00'
destination:
  file:
    name: CA-R-3105-AGENTIC-SCOPE_UNIT_DECLARATION--declare-skills.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-22_FEATURE_AGENTIC/04_requirement
---
## Summary

Declare SKILLS

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import ScopeUnit

declare_entity(
    entity_name='SKILLS',
    instance=ScopeUnit(
        id='CA-SU-23',
        name='SKILLS',
        label='FEATURE',
        ordered=False,
        container='AGENTIC',
        structural_level=3,
    ),
)
```
