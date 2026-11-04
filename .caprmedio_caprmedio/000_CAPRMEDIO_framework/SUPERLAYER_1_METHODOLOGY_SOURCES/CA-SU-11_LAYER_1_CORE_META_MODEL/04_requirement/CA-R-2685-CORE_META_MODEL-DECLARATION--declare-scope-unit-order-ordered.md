---
atom_id: CA-R-2685
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Scope Unit.order.ordered
  passive:
  - CAPRMEDIO_MODEL <+ Scope Unit.order
  - CAPRMEDIO_MODEL <+ CFEL <+ Format/bool
version: 1
updated_at: 2026-11-02 19:17:40 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---
## Summary

Declare Scope Unit.order.ordered

## Claim

### Formal Claim

```CFEL
# model
Scope Unit.order.ordered: [bool]{:1};

Scope Unit.order.ordered.*[]{:0}
```

