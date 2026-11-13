---
atom_id: CA-R-2678
ref_id: CA-R-2678@1
role: Requirement
form: Scope Unit Declaration
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_ACTIONS
tier: 3
status: archived
version: 1
updated_at: 2026-11-02 19:07:49 +0400
destination:
  file:
    name: CA-R-2678@1-SINGLE_ACTIONS-DEFINES_SCOPE_FOR-PROJECT_ACTIONS--declare-project-actions.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/CA-SU-31_FEATURE_GROUP_SINGLE_ACTIONS/04_requirement/099_archived
---
## Summary

Declare PROJECT_ACTIONS

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//PROJECT_ACTIONS.ID == "CA-SU-39";

Scope Unit//PROJECT_ACTIONS.Name == "PROJECT_ACTIONS";

Scope Unit//PROJECT_ACTIONS.Label == "FEATURE_GROUP";

Scope Unit//PROJECT_ACTIONS.order.ordered == false;

Scope Unit//PROJECT_ACTIONS ((IS_CONTAINED_BY)) Scope Unit//SINGLE_ACTIONS
```

