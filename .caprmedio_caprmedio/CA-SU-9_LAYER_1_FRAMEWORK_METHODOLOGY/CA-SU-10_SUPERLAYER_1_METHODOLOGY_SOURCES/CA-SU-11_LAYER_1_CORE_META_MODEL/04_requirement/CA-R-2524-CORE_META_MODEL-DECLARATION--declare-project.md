---
atom_id: CA-R-2524
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Project
version: 3
updated_at: 2026-11-02 19:17:40 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---

## Summary

Declare Project

## Claim

A Project uses CAPRMEDIO's MODEL.

```CFEL
Scope Unit/Project;
Scope Unit/Project//{:1};
Project >| (Container == yes);
Project// {:0}((IS_CONTAINED_BY)) Scope Unit//;
Project ((NARROWER_THAN)) @Scope Unit;
Project//.order.ordered == false;
Project//.order.number: []{:0};
Project//.ID: []{:0}
```

## Semantics

A Project is the root Scope Unit. The Project is not renamed or moved through Scope Unit operations. It has no Scope Unit ID. The shared model makes it Unordered with no order.number; individual Project Declarations inherit these facts.
