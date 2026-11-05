---
atom_id: CA-R-2644
ref_id: CA-R-2644
role: Requirement
form: Scope Unit Declaration
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//GET_EXECUTION_CONTEXT
tier: 3
status: Active
version: 1
updated_at: 2026-11-02 19:07:49 +0400
---
## Summary

Declare GET_EXECUTION_CONTEXT

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//GET_EXECUTION_CONTEXT.ID == "CA-SU-5";

Scope Unit//GET_EXECUTION_CONTEXT.Name == "GET_EXECUTION_CONTEXT";

Scope Unit//GET_EXECUTION_CONTEXT.Label == "TOOL";

Scope Unit//GET_EXECUTION_CONTEXT.order.ordered == false;

Scope Unit//GET_EXECUTION_CONTEXT ((IS_CONTAINED_BY)) Scope Unit//TOOLS
```

