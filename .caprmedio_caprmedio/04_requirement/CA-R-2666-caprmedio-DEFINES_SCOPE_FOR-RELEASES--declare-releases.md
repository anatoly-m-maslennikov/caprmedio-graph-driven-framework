---
atom_id: CA-R-2666
ref_id: CA-R-2666
role: Requirement
form: Scope Unit Declaration
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//RELEASES
tier: 3
status: Active
version: 1
updated_at: 2026-11-02 19:07:49 +0400
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

