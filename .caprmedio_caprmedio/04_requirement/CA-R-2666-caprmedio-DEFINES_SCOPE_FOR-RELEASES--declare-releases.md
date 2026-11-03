---
atom_id: CA-R-2666
role: Requirement
form: Scope Unit Declaration
status: Active
version: 1
updated_at: 2026-11-02 19:07:49 +0400
tier: 3
subjects:
  active: CAPRMEDIO_STRUCTURE <+ Scope Unit//RELEASES
relations: {}
---
## Summary

Declare RELEASES

## Claim

```CFEL
Scope Unit//RELEASES.ID == "CA-SU-27";
Scope Unit//RELEASES.Name == "RELEASES";
Scope Unit//RELEASES.Label == "LAYER";
Scope Unit//RELEASES.order.ordered == true;
Scope Unit//RELEASES.order.number == 5;
Scope Unit//RELEASES ((IS_CONTAINED_BY)) Project//caprmedio
```
