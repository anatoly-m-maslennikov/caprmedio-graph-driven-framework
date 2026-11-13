---
atom_id: CA-R-2670
ref_id: CA-R-2670@1
role: Requirement
form: Scope Unit Declaration
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//SINGLE_ACTIONS
tier: 3
status: archived
version: 1
updated_at: 2026-11-02 19:07:49 +0400
destination:
  file:
    name: CA-R-2670@1-TOOLS-DEFINES_SCOPE_FOR-SINGLE_ACTIONS--declare-single-actions.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/04_requirement/099_archived
---
## Summary

Declare SINGLE_ACTIONS

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//SINGLE_ACTIONS.ID == "CA-SU-31";

Scope Unit//SINGLE_ACTIONS.Name == "SINGLE_ACTIONS";

Scope Unit//SINGLE_ACTIONS.Label == "FEATURE_GROUP";

Scope Unit//SINGLE_ACTIONS.order.ordered == false;

Scope Unit//SINGLE_ACTIONS ((IS_CONTAINED_BY)) Scope Unit//TOOLS
```

