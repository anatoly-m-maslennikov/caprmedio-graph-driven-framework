---
atom_id: CA-R-2667
ref_id: CA-R-2667
role: Requirement
form: Scope Unit Declaration
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//COMMUNITY_EXTENSIONS
tier: 3
status: active
version: 2
updated_at: '2026-11-12T18:36:44.625027+00:00'
container:
  scope_unit: CA-SU-00
destination:
  file:
    name: CA-R-2667-SCOPE_UNIT_DECLARATION--declare-community-extensions.md
    path: .caprmedio_caprmedio/04_requirement
---
## Summary

Declare COMMUNITY_EXTENSIONS

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import ScopeUnit

declare_entity(
    entity_name='COMMUNITY_EXTENSIONS',
    instance=ScopeUnit(
        structural_level=1,
        id='CA-SU-28',
        name='COMMUNITY_EXTENSIONS',
        label='FEATURE',
        ordered=False,
        container='caprmedio',
    ),
)
```

