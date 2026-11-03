---
atom_id: CA-R-2608
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL<+Operator//Membership
version: 1
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---

## Summary

Declare CFEL operator in / not in

## Claim

### Formal Claim

```CFEL
# model
Operator//Membership == "in / not in"
```

## Semantics

Test membership or non-membership in a selected set.
