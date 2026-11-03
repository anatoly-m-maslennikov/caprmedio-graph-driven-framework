---
atom_id: CA-R-2645
role: Requirement
form: Scope Unit Declaration
status: Active
version: 1
updated_at: 2026-11-02 19:07:49 +0400
tier: 3
subjects:
  active: CAPRMEDIO_STRUCTURE <+ Scope Unit//GET_EXECUTION_STATUS
relations: {}
---
## Summary

Declare GET_EXECUTION_STATUS

## Claim

```CFEL
Scope Unit//GET_EXECUTION_STATUS.ID == "CA-SU-6";
Scope Unit//GET_EXECUTION_STATUS.Name == "GET_EXECUTION_STATUS";
Scope Unit//GET_EXECUTION_STATUS.Label == "TOOL";
Scope Unit//GET_EXECUTION_STATUS.order.ordered == false;
Scope Unit//GET_EXECUTION_STATUS ((IS_CONTAINED_BY)) Scope Unit//TOOLS
```
