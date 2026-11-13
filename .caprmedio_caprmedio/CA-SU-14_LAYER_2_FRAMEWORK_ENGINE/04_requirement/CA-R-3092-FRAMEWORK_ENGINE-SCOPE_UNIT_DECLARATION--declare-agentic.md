---
identity:
  atom_id: CA-R-3092
  ref_id: CA-R-3092
context:
  role: requirement
  form: scope_unit_declaration
  container:
    scope_unit: CA-SU-14
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//AGENTIC
  tier: 3
state:
  version: 1
  status: active
  updated_at: '2026-11-12T19:26:20.433443+00:00'
destination:
  file:
    name: CA-R-3092-FRAMEWORK_ENGINE-SCOPE_UNIT_DECLARATION--declare-agentic.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/04_requirement
---
## Summary

Declare AGENTIC

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import ScopeUnit

declare_entity(
    entity_name='AGENTIC',
    instance=ScopeUnit(
        id='CA-SU-22',
        name='AGENTIC',
        label='FEATURE',
        ordered=False,
        container='FRAMEWORK_ENGINE',
        structural_level=2,
    ),
)
```
