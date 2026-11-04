---
atom_id: CA-R-2764
role: Requirement
form: Scope Unit Declaration
status: Active
version: 1
updated_at: 2026-11-04 17:55:47 +0400
tier: 3
subjects:
  active: CAPRMEDIO_STRUCTURE <+ Scope Unit//WORKBENCH_FRONTEND
relations: {}
---
## Summary

Declare WORKBENCH_FRONTEND

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//WORKBENCH_FRONTEND.ID == "CA-SU-46";

Scope Unit//WORKBENCH_FRONTEND.Name == "WORKBENCH_FRONTEND";

Scope Unit//WORKBENCH_FRONTEND.Label == "FEATURE";

Scope Unit//WORKBENCH_FRONTEND.order.ordered == false;

Scope Unit//WORKBENCH_FRONTEND ((IS_CONTAINED_BY)) Scope Unit//WORKBENCH
```

### Prose Claim

Own the Workbench query UI, component palette, presentation, formatting, page navigation and frontend state. Shared Workbench requirements and cross-interface contracts remain in WORKBENCH.
