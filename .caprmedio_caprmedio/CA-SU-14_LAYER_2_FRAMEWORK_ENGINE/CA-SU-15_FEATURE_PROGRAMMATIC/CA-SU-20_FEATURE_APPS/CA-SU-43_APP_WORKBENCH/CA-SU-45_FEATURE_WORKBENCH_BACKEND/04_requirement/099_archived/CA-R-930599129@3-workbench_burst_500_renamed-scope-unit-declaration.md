---
atom_id: "CA-R-930599129"
role: Requirement
form: Scope Unit Declaration
status: "Archived"
version: 3
updated_at: "2026-11-12 20:05:47 +0000"
subjects:
  active: "CAPRMEDIO_STRUCTURE <+ Scope Unit//WORKBENCH_BURST_500_RENAMED"
  passive: []
relations: {}
---
## Summary

Declare Scope Unit

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import ScopeUnit

declare_entity(
    entity_name='WORKBENCH_BURST_500_RENAMED',
    instance=ScopeUnit(
        id='CA-SU-910647071',
        name='WORKBENCH_BURST_500_RENAMED',
        structural_level=6,
        label='FEATURE',
        ordered=False,
        container='WORKBENCH_BACKEND',
    ),
)
```
