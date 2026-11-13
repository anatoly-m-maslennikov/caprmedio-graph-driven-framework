---
atom_id: CA-R-2677
ref_id: CA-R-2677@1
role: Requirement
form: Scope Unit Declaration
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//JOURNAL_ACTIONS
tier: 3
status: archived
version: 1
updated_at: 2026-11-02 19:07:49 +0400
destination:
  file:
    name: CA-R-2677@1-SINGLE_ACTIONS-DEFINES_SCOPE_FOR-JOURNAL_ACTIONS--declare-journal-actions.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/CA-SU-31_FEATURE_GROUP_SINGLE_ACTIONS/04_requirement/099_archived
---
## Summary

Declare JOURNAL_ACTIONS

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//JOURNAL_ACTIONS.ID == "CA-SU-38";

Scope Unit//JOURNAL_ACTIONS.Name == "JOURNAL_ACTIONS";

Scope Unit//JOURNAL_ACTIONS.Label == "FEATURE_GROUP";

Scope Unit//JOURNAL_ACTIONS.order.ordered == false;

Scope Unit//JOURNAL_ACTIONS ((IS_CONTAINED_BY)) Scope Unit//SINGLE_ACTIONS
```

