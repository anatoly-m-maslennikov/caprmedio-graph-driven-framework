---
atom_id: CA-R-2680
ref_id: CA-R-2680@1
role: Requirement
form: Scope Unit Declaration
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//BATCH_SCHEDULER
tier: 3
status: archived
version: 1
updated_at: 2026-11-02 19:07:49 +0400
destination:
  file:
    name: CA-R-2680@1-SCHEDULERS-DEFINES_SCOPE_FOR-BATCH_SCHEDULER--declare-batch-scheduler.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/CA-SU-32_FEATURE_GROUP_SCHEDULERS/04_requirement/099_archived
---
## Summary

Declare BATCH_SCHEDULER

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//BATCH_SCHEDULER.ID == "CA-SU-41";

Scope Unit//BATCH_SCHEDULER.Name == "BATCH_SCHEDULER";

Scope Unit//BATCH_SCHEDULER.Label == "FEATURE_GROUP";

Scope Unit//BATCH_SCHEDULER.order.ordered == false;

Scope Unit//BATCH_SCHEDULER ((IS_CONTAINED_BY)) Scope Unit//SCHEDULERS
```

