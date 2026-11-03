---
atom_id: CA-R-2641
role: Requirement
form: Scope Unit Declaration
status: Active
version: 1
updated_at: 2026-11-02 19:07:49 +0400
tier: 3
subjects:
  active: CAPRMEDIO_STRUCTURE <+ Scope Unit//WORKFLOW_ORCHESTRATOR
relations: {}
---
## Summary

Declare WORKFLOW_ORCHESTRATOR

## Claim

```CFEL
Scope Unit//WORKFLOW_ORCHESTRATOR.ID == "CA-SU-2";
Scope Unit//WORKFLOW_ORCHESTRATOR.Name == "WORKFLOW_ORCHESTRATOR";
Scope Unit//WORKFLOW_ORCHESTRATOR.Label == "APP";
Scope Unit//WORKFLOW_ORCHESTRATOR.order.ordered == false;
Scope Unit//WORKFLOW_ORCHESTRATOR ((IS_CONTAINED_BY)) Scope Unit//APPS
```
