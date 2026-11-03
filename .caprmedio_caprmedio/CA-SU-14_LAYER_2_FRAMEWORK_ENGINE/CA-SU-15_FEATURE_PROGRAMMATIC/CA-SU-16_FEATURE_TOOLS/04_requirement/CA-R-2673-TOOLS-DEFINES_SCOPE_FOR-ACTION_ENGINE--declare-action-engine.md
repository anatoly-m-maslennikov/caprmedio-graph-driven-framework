---
atom_id: CA-R-2673
role: Requirement
form: Scope Unit Declaration
status: Active
version: 1
updated_at: 2026-11-02 19:07:49 +0400
tier: 3
subjects:
  active: CAPRMEDIO_STRUCTURE <+ Scope Unit//ACTION_ENGINE
relations: {}
---
## Summary

Declare ACTION_ENGINE

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//ACTION_ENGINE.ID == "CA-SU-34";

Scope Unit//ACTION_ENGINE.Name == "ACTION_ENGINE";

Scope Unit//ACTION_ENGINE.Label == "FEATURE_GROUP";

Scope Unit//ACTION_ENGINE.order.ordered == false;

Scope Unit//ACTION_ENGINE ((IS_CONTAINED_BY)) Scope Unit//TOOLS
```

