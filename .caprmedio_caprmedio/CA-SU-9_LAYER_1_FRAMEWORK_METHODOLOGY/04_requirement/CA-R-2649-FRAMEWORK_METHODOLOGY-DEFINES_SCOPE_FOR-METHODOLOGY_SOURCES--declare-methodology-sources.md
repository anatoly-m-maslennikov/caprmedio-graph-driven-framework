---
atom_id: CA-R-2649
role: Requirement
form: Scope Unit Declaration
status: Active
version: 1
updated_at: 2026-11-02 19:07:49 +0400
tier: 3
subjects:
  active: CAPRMEDIO_STRUCTURE <+ Scope Unit//METHODOLOGY_SOURCES
relations: {}
---
## Summary

Declare METHODOLOGY_SOURCES

## Claim

### Formal Claim

```CFEL
Scope Unit//METHODOLOGY_SOURCES.ID == "CA-SU-10";
Scope Unit//METHODOLOGY_SOURCES.Name == "METHODOLOGY_SOURCES";
Scope Unit//METHODOLOGY_SOURCES.Label == "SUPERLAYER";
Scope Unit//METHODOLOGY_SOURCES.order.ordered == true;
Scope Unit//METHODOLOGY_SOURCES.order.number == 1;
Scope Unit//METHODOLOGY_SOURCES ((IS_CONTAINED_BY)) Scope Unit//FRAMEWORK_METHODOLOGY
```

