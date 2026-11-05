---
atom_id: CA-R-2674
ref_id: CA-R-2674
role: Requirement
form: Scope Unit Declaration
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//ATOM_ACTIONS
tier: 3
status: Active
version: 1
updated_at: 2026-11-02 19:07:49 +0400
---
## Summary

Declare ATOM_ACTIONS

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//ATOM_ACTIONS.ID == "CA-SU-35";

Scope Unit//ATOM_ACTIONS.Name == "ATOM_ACTIONS";

Scope Unit//ATOM_ACTIONS.Label == "FEATURE_GROUP";

Scope Unit//ATOM_ACTIONS.order.ordered == false;

Scope Unit//ATOM_ACTIONS ((IS_CONTAINED_BY)) Scope Unit//SINGLE_ACTIONS
```

