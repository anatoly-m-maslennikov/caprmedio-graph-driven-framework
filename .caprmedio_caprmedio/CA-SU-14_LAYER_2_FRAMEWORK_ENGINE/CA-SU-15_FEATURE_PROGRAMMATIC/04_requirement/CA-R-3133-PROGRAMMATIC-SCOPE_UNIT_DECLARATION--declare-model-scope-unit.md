---
identity:
  atom_id: CA-R-3133
  ref_id: CA-R-3133
context:
  role: requirement
  form: scope_unit_declaration
  tier: 3
  container:
    scope_unit: CA-SU-15
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//MODEL
state:
  version: 1
  status: active
  updated_at: '2026-11-13T15:13:40.388828+00:00'
destination:
  file:
    name: CA-R-3133-PROGRAMMATIC-SCOPE_UNIT_DECLARATION--declare-model-scope-unit.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement
---
## Summary

Declare MODEL Scope Unit

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import ScopeUnit

declare_entity(
    entity_name="MODEL",
    instance=ScopeUnit(
        id="CA-SU-51",
        name="MODEL",
        structural_level=3,
        label='FEATURE',
        ordered=False,
        container="PROGRAMMATIC",
    ),
)
```
