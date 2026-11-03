---
atom_id: CA-R-2652
role: Requirement
form: Scope Unit Declaration
status: Active
version: 1
updated_at: 2026-11-02 19:07:49 +0400
tier: 3
subjects:
  active: CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
relations: {}
---
## Summary

Declare PROJECT_CONFIGURATION

## Claim

```CFEL
Scope Unit//PROJECT_CONFIGURATION.ID == "CA-SU-13";
Scope Unit//PROJECT_CONFIGURATION.Name == "PROJECT_CONFIGURATION";
Scope Unit//PROJECT_CONFIGURATION.Label == "LAYER";
Scope Unit//PROJECT_CONFIGURATION.order.ordered == true;
Scope Unit//PROJECT_CONFIGURATION.order.number == 3;
Scope Unit//PROJECT_CONFIGURATION ((IS_CONTAINED_BY)) Scope Unit//METHODOLOGY_SOURCES
```

