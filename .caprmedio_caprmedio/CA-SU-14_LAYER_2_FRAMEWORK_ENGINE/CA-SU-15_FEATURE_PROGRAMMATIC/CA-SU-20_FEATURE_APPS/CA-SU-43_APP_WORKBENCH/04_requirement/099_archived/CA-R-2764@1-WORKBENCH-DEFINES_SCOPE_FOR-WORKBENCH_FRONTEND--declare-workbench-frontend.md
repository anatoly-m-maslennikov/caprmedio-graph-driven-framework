---
atom_id: CA-R-2764
ref_id: CA-R-2764@1
role: Requirement
form: Scope Unit Declaration
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//WORKBENCH_FRONTEND
tier: 3
status: Archived
version: 1
updated_at: 2026-11-04 17:55:47 +0400
destination:
  file:
    name: CA-R-2764@1-WORKBENCH-DEFINES_SCOPE_FOR-WORKBENCH_FRONTEND--declare-workbench-frontend.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement/archived
---
## Summary

Declare WORKBENCH_FRONTEND

## Claim

### Prose Claim

Own the Workbench query UI, component palette, presentation, formatting, page navigation and frontend state. Shared Workbench requirements and cross-interface contracts remain in WORKBENCH.
### Formal Claim

```CFEL
# instances
Scope Unit//WORKBENCH_FRONTEND.ID == "CA-SU-46";

Scope Unit//WORKBENCH_FRONTEND.Name == "WORKBENCH_FRONTEND";

Scope Unit//WORKBENCH_FRONTEND.Label == "FEATURE";

Scope Unit//WORKBENCH_FRONTEND.order.ordered == false;

Scope Unit//WORKBENCH_FRONTEND ((IS_CONTAINED_BY)) Scope Unit//WORKBENCH
```

