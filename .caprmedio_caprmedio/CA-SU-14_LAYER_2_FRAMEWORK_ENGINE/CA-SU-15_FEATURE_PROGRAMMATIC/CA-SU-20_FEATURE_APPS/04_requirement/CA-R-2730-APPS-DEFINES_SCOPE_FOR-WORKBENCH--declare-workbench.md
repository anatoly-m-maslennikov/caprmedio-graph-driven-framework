---
atom_id: CA-R-2730
role: Requirement
form: Scope Unit Declaration
status: Active
version: 1
updated_at: 2026-11-03 23:17:14 +0400
tier: 3
subjects:
  active: CAPRMEDIO_STRUCTURE <+ Scope Unit//WORKBENCH
relations: {}
---
## Summary

Declare WORKBENCH

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//WORKBENCH.ID == "CA-SU-43";

Scope Unit//WORKBENCH.Name == "WORKBENCH";

Scope Unit//WORKBENCH.Label == "APP";

Scope Unit//WORKBENCH.order.ordered == false;

Scope Unit//WORKBENCH ((IS_CONTAINED_BY)) Scope Unit//APPS
```

