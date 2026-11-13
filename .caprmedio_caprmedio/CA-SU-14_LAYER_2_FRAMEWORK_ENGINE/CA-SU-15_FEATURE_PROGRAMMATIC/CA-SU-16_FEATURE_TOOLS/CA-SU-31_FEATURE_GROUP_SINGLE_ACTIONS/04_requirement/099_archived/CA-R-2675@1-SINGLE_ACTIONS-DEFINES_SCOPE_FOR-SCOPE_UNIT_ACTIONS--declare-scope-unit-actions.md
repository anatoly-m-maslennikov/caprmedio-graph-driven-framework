---
atom_id: CA-R-2675
ref_id: CA-R-2675@1
role: Requirement
form: Scope Unit Declaration
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//SCOPE_UNIT_ACTIONS
tier: 3
status: archived
version: 1
updated_at: 2026-11-02 19:07:49 +0400
destination:
  file:
    name: CA-R-2675@1-SINGLE_ACTIONS-DEFINES_SCOPE_FOR-SCOPE_UNIT_ACTIONS--declare-scope-unit-actions.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/CA-SU-31_FEATURE_GROUP_SINGLE_ACTIONS/04_requirement/099_archived
---
## Summary

Declare SCOPE_UNIT_ACTIONS

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//SCOPE_UNIT_ACTIONS.ID == "CA-SU-36";

Scope Unit//SCOPE_UNIT_ACTIONS.Name == "SCOPE_UNIT_ACTIONS";

Scope Unit//SCOPE_UNIT_ACTIONS.Label == "FEATURE_GROUP";

Scope Unit//SCOPE_UNIT_ACTIONS.order.ordered == false;

Scope Unit//SCOPE_UNIT_ACTIONS ((IS_CONTAINED_BY)) Scope Unit//SINGLE_ACTIONS
```

