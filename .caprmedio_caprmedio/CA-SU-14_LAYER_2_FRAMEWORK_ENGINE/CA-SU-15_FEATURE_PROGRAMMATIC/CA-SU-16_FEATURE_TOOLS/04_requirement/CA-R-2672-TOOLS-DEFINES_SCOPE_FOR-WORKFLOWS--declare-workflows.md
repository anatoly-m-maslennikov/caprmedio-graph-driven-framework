---
atom_id: CA-R-2672
ref_id: CA-R-2672
role: Requirement
form: Scope Unit Declaration
status: Active
version: 1
updated_at: 2026-11-02 19:07:49 +0400
tier: 3
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//WORKFLOWS
---
## Summary

Declare WORKFLOWS

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//WORKFLOWS.ID == "CA-SU-33";

Scope Unit//WORKFLOWS.Name == "WORKFLOWS";

Scope Unit//WORKFLOWS.Label == "FEATURE_GROUP";

Scope Unit//WORKFLOWS.order.ordered == false;

Scope Unit//WORKFLOWS ((IS_CONTAINED_BY)) Scope Unit//TOOLS
```

