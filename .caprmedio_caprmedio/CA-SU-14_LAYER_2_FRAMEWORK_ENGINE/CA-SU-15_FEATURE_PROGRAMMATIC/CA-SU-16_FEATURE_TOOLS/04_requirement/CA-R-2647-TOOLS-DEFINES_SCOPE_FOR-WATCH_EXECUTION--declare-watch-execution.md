---
atom_id: CA-R-2647
ref_id: CA-R-2647
role: Requirement
form: Scope Unit Declaration
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//WATCH_EXECUTION
tier: 3
status: Active
version: 1
updated_at: 2026-11-02 19:07:49 +0400
---
## Summary

Declare WATCH_EXECUTION

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//WATCH_EXECUTION.ID == "CA-SU-8";

Scope Unit//WATCH_EXECUTION.Name == "WATCH_EXECUTION";

Scope Unit//WATCH_EXECUTION.Label == "TOOL";

Scope Unit//WATCH_EXECUTION.order.ordered == false;

Scope Unit//WATCH_EXECUTION ((IS_CONTAINED_BY)) Scope Unit//TOOLS
```

