---
atom_id: CA-R-2640
ref_id: CA-R-2640
container:
  scope_unit: CA-SU--1
role: Requirement
form: Scope Unit Declaration
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Project//caprmedio
tier: 3
status: active
version: 2
updated_at: 2026-11-05 12:58:42 +0400
carrier_destination:
  file:
    name: CA-R-2640-ANATOLY-MASLENNIKOV-DEFINES_SCOPE_FOR-caprmedio--declare-caprmedio.md
    path: .caprmedio_caprmedio
---
## Summary

Declare caprmedio

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import Project

declare_entity(
    entity_name='caprmedio',
    instance=Project(
        id='CA-SU-00',
        name='caprmedio',
        structural_level=0,
    ),
)
```
