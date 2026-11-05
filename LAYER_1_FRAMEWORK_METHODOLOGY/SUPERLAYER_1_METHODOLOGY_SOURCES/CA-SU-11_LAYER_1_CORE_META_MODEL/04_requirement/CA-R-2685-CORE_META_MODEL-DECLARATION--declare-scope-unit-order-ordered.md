---
atom_id: CA-R-2685
ref_id: CA-R-2685
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit.order.ordered
  dependencies:
  - CAPRMEDIO_MODEL <+ Scope Unit.order
  - CAPRMEDIO_MODEL <+ CFEL <+ Format/bool
tier: 3
status: Active
version: 1
updated_at: 2026-11-02 19:17:40 +0400
---
## Summary

Declare Scope Unit.order.ordered

## Claim

### Formal Claim

```CFEL
# model
Scope Unit.order.ordered:: [bool]{::1};

Scope Unit.order.ordered.*[]{::0}
```

