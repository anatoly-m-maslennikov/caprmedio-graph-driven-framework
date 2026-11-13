---
atom_id: CA-R-2671
ref_id: CA-R-2671@1
role: Requirement
form: Scope Unit Declaration
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//SCHEDULERS
tier: 3
status: archived
version: 1
updated_at: 2026-11-02 19:07:49 +0400
destination:
  file:
    name: CA-R-2671@1-TOOLS-DEFINES_SCOPE_FOR-SCHEDULERS--declare-schedulers.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/04_requirement/099_archived
---
## Summary

Declare SCHEDULERS

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//SCHEDULERS.ID == "CA-SU-32";

Scope Unit//SCHEDULERS.Name == "SCHEDULERS";

Scope Unit//SCHEDULERS.Label == "FEATURE_GROUP";

Scope Unit//SCHEDULERS.order.ordered == false;

Scope Unit//SCHEDULERS ((IS_CONTAINED_BY)) Scope Unit//TOOLS
```

