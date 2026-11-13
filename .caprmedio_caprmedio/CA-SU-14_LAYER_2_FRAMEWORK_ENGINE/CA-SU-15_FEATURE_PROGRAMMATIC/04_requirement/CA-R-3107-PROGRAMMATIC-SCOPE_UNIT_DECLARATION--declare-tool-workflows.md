---
identity:
  atom_id: CA-R-3107
  ref_id: CA-R-3107
context:
  role: requirement
  form: scope_unit_declaration
  container:
    scope_unit: CA-SU-15
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//TOOL_WORKFLOWS
  tier: 3
state:
  version: 1
  status: active
  updated_at: '2026-11-12T19:27:07.676831+00:00'
destination:
  file:
    name: CA-R-3107-PROGRAMMATIC-SCOPE_UNIT_DECLARATION--declare-tool-workflows.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement
---
## Summary

Declare TOOL_WORKFLOWS

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import ScopeUnit

declare_entity(
    entity_name='TOOL_WORKFLOWS',
    instance=ScopeUnit(
        id='CA-SU-18',
        name='TOOL_WORKFLOWS',
        label='FEATURE',
        ordered=False,
        container='PROGRAMMATIC',
        structural_level=3,
    ),
)
```
