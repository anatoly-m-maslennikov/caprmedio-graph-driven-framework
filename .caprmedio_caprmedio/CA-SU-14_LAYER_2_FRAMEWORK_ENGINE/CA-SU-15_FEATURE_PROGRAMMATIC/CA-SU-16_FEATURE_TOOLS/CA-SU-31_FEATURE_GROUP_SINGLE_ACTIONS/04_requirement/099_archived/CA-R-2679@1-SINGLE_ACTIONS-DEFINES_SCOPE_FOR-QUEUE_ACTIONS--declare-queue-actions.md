---
atom_id: CA-R-2679
ref_id: CA-R-2679@1
role: Requirement
form: Scope Unit Declaration
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//QUEUE_ACTIONS
tier: 3
status: archived
version: 1
updated_at: 2026-11-02 19:07:49 +0400
destination:
  file:
    name: CA-R-2679@1-SINGLE_ACTIONS-DEFINES_SCOPE_FOR-QUEUE_ACTIONS--declare-queue-actions.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/CA-SU-31_FEATURE_GROUP_SINGLE_ACTIONS/04_requirement/099_archived
---
## Summary

Declare QUEUE_ACTIONS

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//QUEUE_ACTIONS.ID == "CA-SU-40";

Scope Unit//QUEUE_ACTIONS.Name == "QUEUE_ACTIONS";

Scope Unit//QUEUE_ACTIONS.Label == "FEATURE_GROUP";

Scope Unit//QUEUE_ACTIONS.order.ordered == false;

Scope Unit//QUEUE_ACTIONS ((IS_CONTAINED_BY)) Scope Unit//SINGLE_ACTIONS
```

