---
identity:
  atom_id: CA-R-3135
  ref_id: CA-R-3135
context:
  role: requirement
  form: scope_unit_declaration
  tier: 3
  container:
    scope_unit: CA-SU-51
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//GENERATED_MODEL
state:
  version: 1
  status: active
  updated_at: '2026-11-13T15:13:45.418497+00:00'
destination:
  file:
    name: CA-R-3135-MODEL-SCOPE_UNIT_DECLARATION--declare-generated-model-scope-unit.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-51_FEATURE_MODEL/04_requirement
---
## Summary

Declare GENERATED MODEL Scope Unit

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import ScopeUnit

declare_entity(
    entity_name="GENERATED_MODEL",
    instance=ScopeUnit(
        id="CA-SU-52",
        name="GENERATED_MODEL",
        structural_level=4,
        label='FEATURE',
        ordered=False,
        container="MODEL",
    ),
)
```
