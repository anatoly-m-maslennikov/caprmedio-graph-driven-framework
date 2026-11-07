---
atom_id: CA-R-2524
ref_id: CA-R-2524
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project
tier: 3
status: Active
version: 6
updated_at: "2026-11-07 15:18:44 +0400"
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-R-2524-CORE_META_MODEL-DECLARATION--declare-project.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---

## Summary

Declare Project

## Claim

### Prose Claim

A Project uses CAPRMEDIO's MODEL.

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

Project//$project_3.order.number:: []{::0}
```

## Semantics

A Project is the root Scope Unit. It is not renamed or moved through Scope Unit operations. Its one stable Scope Unit ID is governed by CA-R-2526. The shared model makes Project unordered with no order.number; individual Project Declarations inherit these facts.
