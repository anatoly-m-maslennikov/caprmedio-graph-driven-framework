---
atom_id: CA-R-2664
ref_id: CA-R-2664@1
role: Requirement
form: Scope Unit Declaration
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//OPERATOR_DOCUMENTATION
tier: 3
status: archived
version: 1
updated_at: 2026-11-02 19:07:49 +0400
destination:
  file:
    name: CA-R-2664@1-caprmedio-DEFINES_SCOPE_FOR-OPERATOR_DOCUMENTATION--declare-operator-documentation.md
    path: .caprmedio_caprmedio/04_requirement/099_archived
---
## Summary

Declare OPERATOR_DOCUMENTATION

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//OPERATOR_DOCUMENTATION.ID == "CA-SU-25";

Scope Unit//OPERATOR_DOCUMENTATION.Name == "OPERATOR_DOCUMENTATION";

Scope Unit//OPERATOR_DOCUMENTATION.Label == "LAYER";

Scope Unit//OPERATOR_DOCUMENTATION.order.ordered == true;

Scope Unit//OPERATOR_DOCUMENTATION.order.number == 3;

Scope Unit//OPERATOR_DOCUMENTATION ((IS_CONTAINED_BY)) Project//caprmedio
```

