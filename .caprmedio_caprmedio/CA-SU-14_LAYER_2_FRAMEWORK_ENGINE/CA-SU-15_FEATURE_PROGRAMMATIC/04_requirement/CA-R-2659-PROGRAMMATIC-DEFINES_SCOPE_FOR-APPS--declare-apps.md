---
atom_id: CA-R-2659
role: Requirement
form: Scope Unit Declaration
status: Active
version: 1
updated_at: 2026-11-02 19:07:49 +0400
tier: 3
subjects:
  active: CAPRMEDIO_STRUCTURE <+ Scope Unit//APPS
relations: {}
---
## Summary

Declare APPS

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//APPS.ID == "CA-SU-20";

Scope Unit//APPS.Name == "APPS";

Scope Unit//APPS.Label == "FEATURE";

Scope Unit//APPS.order.ordered == false;

Scope Unit//APPS ((IS_CONTAINED_BY)) Scope Unit//PROGRAMMATIC
```

