---
atom_id: CA-R-2659
ref_id: CA-R-2659@1
role: Requirement
form: Scope Unit Declaration
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//APPS
tier: 3
status: Archived
version: 1
updated_at: 2026-11-02 19:07:49 +0400
destination:
  file:
    name: CA-R-2659@1-PROGRAMMATIC-DEFINES_SCOPE_FOR-APPS--declare-apps.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement/archived
---
## Summary

Declare APPS

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//APPS.ID == "CA-SU-20";

Scope Unit//APPS.Name == "APPS";

Scope Unit//APPS.Label == "FEATURE";

Scope Unit//APPS.order.ordered == false;

Scope Unit//APPS ((IS_CONTAINED_BY)) Scope Unit//PROGRAMMATIC
```

