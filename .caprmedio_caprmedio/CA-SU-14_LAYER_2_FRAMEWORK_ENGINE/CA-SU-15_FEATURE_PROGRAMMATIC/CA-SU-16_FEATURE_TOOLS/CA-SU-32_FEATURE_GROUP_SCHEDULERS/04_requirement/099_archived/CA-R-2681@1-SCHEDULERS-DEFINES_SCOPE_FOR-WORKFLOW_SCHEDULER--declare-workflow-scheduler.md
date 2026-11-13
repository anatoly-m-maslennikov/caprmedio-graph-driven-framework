---
atom_id: CA-R-2681
ref_id: CA-R-2681@1
role: Requirement
form: Scope Unit Declaration
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//WORKFLOW_SCHEDULER
tier: 3
status: archived
version: 1
updated_at: 2026-11-02 19:07:49 +0400
destination:
  file:
    name: CA-R-2681@1-SCHEDULERS-DEFINES_SCOPE_FOR-WORKFLOW_SCHEDULER--declare-workflow-scheduler.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/CA-SU-32_FEATURE_GROUP_SCHEDULERS/04_requirement/099_archived
---
## Summary

Declare WORKFLOW_SCHEDULER

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//WORKFLOW_SCHEDULER.ID == "CA-SU-42";

Scope Unit//WORKFLOW_SCHEDULER.Name == "WORKFLOW_SCHEDULER";

Scope Unit//WORKFLOW_SCHEDULER.Label == "FEATURE_GROUP";

Scope Unit//WORKFLOW_SCHEDULER.order.ordered == false;

Scope Unit//WORKFLOW_SCHEDULER ((IS_CONTAINED_BY)) Scope Unit//SCHEDULERS
```

