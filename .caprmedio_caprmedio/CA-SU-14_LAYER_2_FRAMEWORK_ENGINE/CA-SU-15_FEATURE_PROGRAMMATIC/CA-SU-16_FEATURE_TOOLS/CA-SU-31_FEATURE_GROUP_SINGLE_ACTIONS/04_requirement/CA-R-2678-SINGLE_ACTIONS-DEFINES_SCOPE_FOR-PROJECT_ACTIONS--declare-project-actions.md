---
atom_id: CA-R-2678
role: Requirement
form: Scope Unit Declaration
status: Active
version: 1
updated_at: 2026-11-02 19:07:49 +0400
tier: 3
subjects:
  active: CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_ACTIONS
relations: {}
---
## Summary

Declare PROJECT_ACTIONS

## Claim

```CFEL
Scope Unit//PROJECT_ACTIONS.ID == "CA-SU-39";
Scope Unit//PROJECT_ACTIONS.Name == "PROJECT_ACTIONS";
Scope Unit//PROJECT_ACTIONS.Label == "FEATURE_GROUP";
Scope Unit//PROJECT_ACTIONS.order.ordered == false;
Scope Unit//PROJECT_ACTIONS ((IS_CONTAINED_BY)) Scope Unit//SINGLE_ACTIONS
```
