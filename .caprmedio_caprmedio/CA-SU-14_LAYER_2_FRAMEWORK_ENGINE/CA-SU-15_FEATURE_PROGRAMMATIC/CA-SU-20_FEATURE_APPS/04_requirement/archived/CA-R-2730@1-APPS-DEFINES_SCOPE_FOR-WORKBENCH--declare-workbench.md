---
atom_id: CA-R-2730
ref_id: CA-R-2730@1
role: Requirement
form: Scope Unit Declaration
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//WORKBENCH
tier: 3
status: Archived
version: 1
updated_at: 2026-11-03 23:17:14 +0400
destination:
  file:
    name: CA-R-2730@1-APPS-DEFINES_SCOPE_FOR-WORKBENCH--declare-workbench.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/04_requirement/archived
---
## Summary

Declare WORKBENCH

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//WORKBENCH.ID == "CA-SU-43";

Scope Unit//WORKBENCH.Name == "WORKBENCH";

Scope Unit//WORKBENCH.Label == "APP";

Scope Unit//WORKBENCH.order.ordered == false;

Scope Unit//WORKBENCH ((IS_CONTAINED_BY)) Scope Unit//APPS
```

