---
atom_id: CA-R-2681
role: Requirement
form: Scope Unit Declaration
status: Active
version: 1
updated_at: 2026-11-02 19:07:49 +0400
tier: 3
subjects:
  active: CAPRMEDIO_STRUCTURE <+ Scope Unit//WORKFLOW_SCHEDULER
relations: {}
---
## Summary

Declare WORKFLOW_SCHEDULER

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//WORKFLOW_SCHEDULER.ID == "CA-SU-42";

Scope Unit//WORKFLOW_SCHEDULER.Name == "WORKFLOW_SCHEDULER";

Scope Unit//WORKFLOW_SCHEDULER.Label == "FEATURE_GROUP";

Scope Unit//WORKFLOW_SCHEDULER.order.ordered == false;

Scope Unit//WORKFLOW_SCHEDULER ((IS_CONTAINED_BY)) Scope Unit//SCHEDULERS
```

