---
atom_id: CA-R-2642
role: Requirement
form: Scope Unit Declaration
status: Active
version: 1
updated_at: 2026-11-02 19:07:49 +0400
tier: 3
subjects:
  active: CAPRMEDIO_STRUCTURE <+ Scope Unit//DISCOVER_TOOLS
relations: {}
---
## Summary

Declare DISCOVER_TOOLS

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//DISCOVER_TOOLS.ID == "CA-SU-3";

Scope Unit//DISCOVER_TOOLS.Name == "DISCOVER_TOOLS";

Scope Unit//DISCOVER_TOOLS.Label == "TOOL";

Scope Unit//DISCOVER_TOOLS.order.ordered == false;

Scope Unit//DISCOVER_TOOLS ((IS_CONTAINED_BY)) Scope Unit//TOOLS
```

