---
atom_id: CA-R-2687
role: Requirement
form: Declaration
status: Active
version: 1
updated_at: 2026-11-02 19:17:40 +0400
tier: 3
subjects:
  active: Scope Unit.order
  passive:
  - Scope Unit
relations: {}
---
## Summary

Declare Scope Unit.order

## Claim

```CFEL
Scope Unit.order: []{:0};
Scope Unit.order.*[in (ordered, number)]{:1..2}
```

## Semantics

order groups the Boolean ordered and the conditional number as sibling Properties. The group has no direct value.
