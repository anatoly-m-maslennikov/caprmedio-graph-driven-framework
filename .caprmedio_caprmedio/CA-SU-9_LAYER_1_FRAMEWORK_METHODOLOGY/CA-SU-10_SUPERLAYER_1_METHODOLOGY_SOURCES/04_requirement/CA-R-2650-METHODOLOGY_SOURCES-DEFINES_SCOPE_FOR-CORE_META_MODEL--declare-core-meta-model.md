---
atom_id: CA-R-2650
role: Requirement
form: Scope Unit Declaration
status: Active
version: 1
updated_at: 2026-11-02 19:07:49 +0400
tier: 3
subjects:
  active: CAPRMEDIO_STRUCTURE <+ Scope Unit//CORE_META_MODEL
relations: {}
---
## Summary

Declare CORE_META_MODEL

## Claim

```CFEL
Scope Unit//CORE_META_MODEL.ID == "CA-SU-11";
Scope Unit//CORE_META_MODEL.Name == "CORE_META_MODEL";
Scope Unit//CORE_META_MODEL.Label == "LAYER";
Scope Unit//CORE_META_MODEL.order.ordered == true;
Scope Unit//CORE_META_MODEL.order.number == 1;
Scope Unit//CORE_META_MODEL ((IS_CONTAINED_BY)) Scope Unit//METHODOLOGY_SOURCES
```

