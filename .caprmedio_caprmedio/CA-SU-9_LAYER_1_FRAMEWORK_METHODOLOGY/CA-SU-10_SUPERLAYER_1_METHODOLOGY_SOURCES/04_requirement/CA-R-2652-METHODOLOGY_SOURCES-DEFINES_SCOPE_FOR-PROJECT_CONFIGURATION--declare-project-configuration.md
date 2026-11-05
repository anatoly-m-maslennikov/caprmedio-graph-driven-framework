---
atom_id: CA-R-2652
ref_id: CA-R-2652
role: Requirement
form: Scope Unit Declaration
status: Active
version: 1
updated_at: 2026-11-02 19:07:49 +0400
tier: 3
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
---
## Summary

Declare PROJECT_CONFIGURATION

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//PROJECT_CONFIGURATION.ID == "CA-SU-13";

Scope Unit//PROJECT_CONFIGURATION.Name == "PROJECT_CONFIGURATION";

Scope Unit//PROJECT_CONFIGURATION.Label == "LAYER";

Scope Unit//PROJECT_CONFIGURATION.order.ordered == true;

Scope Unit//PROJECT_CONFIGURATION.order.number == 3;

Scope Unit//PROJECT_CONFIGURATION ((IS_CONTAINED_BY)) Scope Unit//METHODOLOGY_SOURCES
```

