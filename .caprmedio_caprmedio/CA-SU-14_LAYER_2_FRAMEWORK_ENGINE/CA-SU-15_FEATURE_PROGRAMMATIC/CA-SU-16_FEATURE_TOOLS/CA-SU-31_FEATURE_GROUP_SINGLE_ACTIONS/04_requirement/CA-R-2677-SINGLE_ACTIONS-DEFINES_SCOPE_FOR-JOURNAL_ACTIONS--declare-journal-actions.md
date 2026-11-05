---
atom_id: CA-R-2677
ref_id: CA-R-2677
role: Requirement
form: Scope Unit Declaration
status: Active
version: 1
updated_at: 2026-11-02 19:07:49 +0400
tier: 3
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//JOURNAL_ACTIONS
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

