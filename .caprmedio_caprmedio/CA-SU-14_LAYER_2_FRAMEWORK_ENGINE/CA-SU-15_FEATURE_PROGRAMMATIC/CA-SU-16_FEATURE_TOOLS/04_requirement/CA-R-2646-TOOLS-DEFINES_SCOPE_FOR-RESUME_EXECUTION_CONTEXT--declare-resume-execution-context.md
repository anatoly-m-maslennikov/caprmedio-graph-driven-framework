---
atom_id: CA-R-2646
role: Requirement
form: Scope Unit Declaration
status: Active
version: 1
updated_at: 2026-11-02 19:07:49 +0400
tier: 3
subjects:
  active: CAPRMEDIO_STRUCTURE <+ Scope Unit//RESUME_EXECUTION_CONTEXT
relations: {}
---
## Summary

Declare RESUME_EXECUTION_CONTEXT

## Claim

```CFEL
Scope Unit//RESUME_EXECUTION_CONTEXT.ID == "CA-SU-7";
Scope Unit//RESUME_EXECUTION_CONTEXT.Name == "RESUME_EXECUTION_CONTEXT";
Scope Unit//RESUME_EXECUTION_CONTEXT.Label == "TOOL";
Scope Unit//RESUME_EXECUTION_CONTEXT.order.ordered == false;
Scope Unit//RESUME_EXECUTION_CONTEXT ((IS_CONTAINED_BY)) Scope Unit//TOOLS
```
