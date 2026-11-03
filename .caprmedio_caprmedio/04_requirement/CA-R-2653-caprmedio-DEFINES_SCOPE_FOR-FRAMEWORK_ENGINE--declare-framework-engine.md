---
atom_id: CA-R-2653
role: Requirement
form: Scope Unit Declaration
status: Active
version: 1
updated_at: 2026-11-02 19:07:49 +0400
tier: 3
subjects:
  active: CAPRMEDIO_STRUCTURE <+ Scope Unit//FRAMEWORK_ENGINE
relations: {}
---
## Summary

Declare FRAMEWORK_ENGINE

## Claim

```CFEL
Scope Unit//FRAMEWORK_ENGINE.ID == "CA-SU-14";
Scope Unit//FRAMEWORK_ENGINE.Name == "FRAMEWORK_ENGINE";
Scope Unit//FRAMEWORK_ENGINE.Label == "LAYER";
Scope Unit//FRAMEWORK_ENGINE.order.ordered == true;
Scope Unit//FRAMEWORK_ENGINE.order.number == 2;
Scope Unit//FRAMEWORK_ENGINE ((IS_CONTAINED_BY)) Project//caprmedio
```
