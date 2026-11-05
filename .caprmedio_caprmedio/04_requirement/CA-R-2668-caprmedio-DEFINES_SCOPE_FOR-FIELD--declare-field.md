---
atom_id: CA-R-2668
ref_id: CA-R-2668
role: Requirement
form: Scope Unit Declaration
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//FIELD
tier: 3
status: Active
version: 1
updated_at: 2026-11-02 19:07:49 +0400
---
## Summary

Declare FIELD

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//FIELD.ID == "CA-SU-29";

Scope Unit//FIELD.Name == "FIELD";

Scope Unit//FIELD.Label == "FEATURE";

Scope Unit//FIELD.order.ordered == false;

Scope Unit//FIELD ((IS_CONTAINED_BY)) Project//caprmedio
```

