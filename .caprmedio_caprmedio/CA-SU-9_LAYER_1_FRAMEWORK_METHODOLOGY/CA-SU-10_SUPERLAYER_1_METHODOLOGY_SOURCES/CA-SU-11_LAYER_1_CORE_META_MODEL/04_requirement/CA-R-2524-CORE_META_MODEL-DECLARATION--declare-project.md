---
atom_id: CA-R-2524
ref_id: CA-R-2524
status: Active
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project
version: 3
updated_at: 2026-11-02 19:17:40 +0400
tier: 3
role: Requirement
form: Declaration
---

## Summary

Declare Project

## Claim

### Formal Claim

```CFEL
# model
Scope Unit/Project;

Project >| (Container == yes);

Project ((NARROWER_THAN)) Scope Unit;

# instances
Scope Unit/Project//$scope_unit{::1};

Project//$project {::0}((IS_CONTAINED_BY)) Scope Unit//$scope_unit_2;

Project//$project_2.order.ordered == false;

Project//$project_3.order.number:: []{::0};

Project//$project_4.ID:: []{::0}
```

### Prose Claim


A Project uses CAPRMEDIO's MODEL.


## Semantics

A Project is the root Scope Unit. The Project is not renamed or moved through Scope Unit operations. It has no Scope Unit ID. The shared model makes it Unordered with no order.number; individual Project Declarations inherit these facts.
