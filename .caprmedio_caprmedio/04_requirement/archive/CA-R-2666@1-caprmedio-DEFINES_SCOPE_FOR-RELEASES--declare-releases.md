---
atom_id: CA-R-2666@1
ref_id: CA-R-2666@1
role: Requirement
form: Scope Unit Declaration
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//RELEASES
tier: 3
status: Archived
version: 1
updated_at: 2026-11-02 19:07:49 +0400
destination:
  file:
    name: CA-R-2666@1-caprmedio-DEFINES_SCOPE_FOR-RELEASES--declare-releases.md
    path: .caprmedio_caprmedio/04_requirement/archive
---
## Summary

Declare RELEASES

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//RELEASES.ID == "CA-SU-27";

Scope Unit//RELEASES.Name == "RELEASES";

Scope Unit//RELEASES.Label == "LAYER";

Scope Unit//RELEASES.order.ordered == true;

Scope Unit//RELEASES.order.number == 5;

Scope Unit//RELEASES ((IS_CONTAINED_BY)) Project//caprmedio
```

