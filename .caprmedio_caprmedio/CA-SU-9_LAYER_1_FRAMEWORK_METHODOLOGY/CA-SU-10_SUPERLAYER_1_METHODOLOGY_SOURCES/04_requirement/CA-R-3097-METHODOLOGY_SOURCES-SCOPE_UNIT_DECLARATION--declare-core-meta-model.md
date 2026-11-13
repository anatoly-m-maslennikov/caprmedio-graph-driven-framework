---
identity:
  atom_id: CA-R-3097
  ref_id: CA-R-3097
context:
  role: requirement
  form: scope_unit_declaration
  container:
    scope_unit: CA-SU-10
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//CORE_META_MODEL
  tier: 3
state:
  version: 1
  status: active
  updated_at: '2026-11-12T19:26:32.188977+00:00'
destination:
  file:
    name: CA-R-3097-METHODOLOGY_SOURCES-SCOPE_UNIT_DECLARATION--declare-core-meta-model.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/04_requirement
---
## Summary

Declare CORE_META_MODEL

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import ScopeUnit

declare_entity(
    entity_name='CORE_META_MODEL',
    instance=ScopeUnit(
        id='CA-SU-11',
        name='CORE_META_MODEL',
        label='LAYER',
        ordered=True,
        order_number=1,
        container='METHODOLOGY_SOURCES',
        structural_level=3,
    ),
)
```
