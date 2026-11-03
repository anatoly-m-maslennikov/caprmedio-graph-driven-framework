---
atom_id: CA-R-2643
role: Requirement
form: Scope Unit Declaration
status: Active
version: 1
updated_at: 2026-11-02 19:07:49 +0400
tier: 3
subjects:
  active: CAPRMEDIO_STRUCTURE <+ Scope Unit//DISCOVER_OPERATIONS
relations: {}
---
## Summary

Declare DISCOVER_OPERATIONS

## Claim

### Formal Claim

```CFEL
Scope Unit//DISCOVER_OPERATIONS.ID == "CA-SU-4";
Scope Unit//DISCOVER_OPERATIONS.Name == "DISCOVER_OPERATIONS";
Scope Unit//DISCOVER_OPERATIONS.Label == "TOOL";
Scope Unit//DISCOVER_OPERATIONS.order.ordered == false;
Scope Unit//DISCOVER_OPERATIONS ((IS_CONTAINED_BY)) Scope Unit//TOOLS
```

