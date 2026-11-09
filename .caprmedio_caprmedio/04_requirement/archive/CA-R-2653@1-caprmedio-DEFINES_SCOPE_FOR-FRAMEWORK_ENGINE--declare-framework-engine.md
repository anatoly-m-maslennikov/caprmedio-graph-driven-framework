---
atom_id: CA-R-2653@1
ref_id: CA-R-2653@1
role: Requirement
form: Scope Unit Declaration
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//FRAMEWORK_ENGINE
tier: 3
status: Archived
version: 1
updated_at: 2026-11-02 19:07:49 +0400
destination:
  file:
    name: CA-R-2653@1-caprmedio-DEFINES_SCOPE_FOR-FRAMEWORK_ENGINE--declare-framework-engine.md
    path: .caprmedio_caprmedio/04_requirement/archive
---
## Summary

Declare FRAMEWORK_ENGINE

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//FRAMEWORK_ENGINE.ID == "CA-SU-14";

Scope Unit//FRAMEWORK_ENGINE.Name == "FRAMEWORK_ENGINE";

Scope Unit//FRAMEWORK_ENGINE.Label == "LAYER";

Scope Unit//FRAMEWORK_ENGINE.order.ordered == true;

Scope Unit//FRAMEWORK_ENGINE.order.number == 2;

Scope Unit//FRAMEWORK_ENGINE ((IS_CONTAINED_BY)) Project//caprmedio
```

