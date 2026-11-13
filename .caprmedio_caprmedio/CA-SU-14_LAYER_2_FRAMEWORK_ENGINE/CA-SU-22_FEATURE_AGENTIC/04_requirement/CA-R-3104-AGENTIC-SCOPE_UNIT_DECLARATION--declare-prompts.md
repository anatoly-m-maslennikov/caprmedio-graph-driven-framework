---
identity:
  atom_id: CA-R-3104
  ref_id: CA-R-3104
context:
  role: requirement
  form: scope_unit_declaration
  container:
    scope_unit: CA-SU-22
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//PROMPTS
  tier: 3
state:
  version: 1
  status: active
  updated_at: '2026-11-12T19:27:00.223904+00:00'
destination:
  file:
    name: CA-R-3104-AGENTIC-SCOPE_UNIT_DECLARATION--declare-prompts.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-22_FEATURE_AGENTIC/04_requirement
---
## Summary

Declare PROMPTS

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import ScopeUnit

declare_entity(
    entity_name='PROMPTS',
    instance=ScopeUnit(
        id='CA-SU-24',
        name='PROMPTS',
        label='FEATURE',
        ordered=False,
        container='AGENTIC',
        structural_level=3,
    ),
)
```
