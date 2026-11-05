---
atom_id: CA-R-2679
ref_id: CA-R-2679
role: Requirement
form: Scope Unit Declaration
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//QUEUE_ACTIONS
tier: 3
status: Active
version: 1
updated_at: 2026-11-02 19:07:49 +0400
---
## Summary

Declare QUEUE_ACTIONS

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//QUEUE_ACTIONS.ID == "CA-SU-40";

Scope Unit//QUEUE_ACTIONS.Name == "QUEUE_ACTIONS";

Scope Unit//QUEUE_ACTIONS.Label == "FEATURE_GROUP";

Scope Unit//QUEUE_ACTIONS.order.ordered == false;

Scope Unit//QUEUE_ACTIONS ((IS_CONTAINED_BY)) Scope Unit//SINGLE_ACTIONS
```

