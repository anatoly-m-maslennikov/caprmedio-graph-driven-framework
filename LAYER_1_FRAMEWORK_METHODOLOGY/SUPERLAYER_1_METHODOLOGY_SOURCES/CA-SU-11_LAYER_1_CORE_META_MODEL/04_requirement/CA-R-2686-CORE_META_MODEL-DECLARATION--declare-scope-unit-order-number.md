---
atom_id: CA-R-2686
ref_id: CA-R-2686
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit.order.number
  dependencies:
  - CAPRMEDIO_MODEL <+ Scope Unit.order
  - CAPRMEDIO_MODEL <+ Scope Unit.order.ordered
  - CAPRMEDIO_MODEL <+ CFEL <+ Format/int
tier: 3
status: Active
version: 1
updated_at: 2026-11-02 19:17:40 +0400
---
## Summary

Declare Scope Unit.order.number

## Claim

### Formal Claim

```CFEL
# model
Scope Unit.order.number: IF order.ordered = true THEN [int, 1+]{::1} ELSE []{::0};

Scope Unit.order.number.*[]{::0}
```

## Semantics

`order.ordered` is the Boolean value on the same Scope Unit. `1+` admits integer values of at least 1; `{:1}` requires one value. When order.ordered is false, order.number has no value.

The number is the position among ordered siblings with the same direct parent. Displayed positions do not establish parentage, ownership or Atom authority.
