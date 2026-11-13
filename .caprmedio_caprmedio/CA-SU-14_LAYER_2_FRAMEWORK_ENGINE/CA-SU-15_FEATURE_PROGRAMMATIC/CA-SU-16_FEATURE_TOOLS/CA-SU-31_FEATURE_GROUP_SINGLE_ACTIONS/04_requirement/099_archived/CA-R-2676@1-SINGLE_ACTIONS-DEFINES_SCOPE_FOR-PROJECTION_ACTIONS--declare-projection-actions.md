---
atom_id: CA-R-2676
ref_id: CA-R-2676@1
role: Requirement
form: Scope Unit Declaration
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECTION_ACTIONS
tier: 3
status: archived
version: 1
updated_at: 2026-11-02 19:07:49 +0400
destination:
  file:
    name: CA-R-2676@1-SINGLE_ACTIONS-DEFINES_SCOPE_FOR-PROJECTION_ACTIONS--declare-projection-actions.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/CA-SU-31_FEATURE_GROUP_SINGLE_ACTIONS/04_requirement/099_archived
---
## Summary

Declare PROJECTION_ACTIONS

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//PROJECTION_ACTIONS.ID == "CA-SU-37";

Scope Unit//PROJECTION_ACTIONS.Name == "PROJECTION_ACTIONS";

Scope Unit//PROJECTION_ACTIONS.Label == "FEATURE_GROUP";

Scope Unit//PROJECTION_ACTIONS.order.ordered == false;

Scope Unit//PROJECTION_ACTIONS ((IS_CONTAINED_BY)) Scope Unit//SINGLE_ACTIONS
```

