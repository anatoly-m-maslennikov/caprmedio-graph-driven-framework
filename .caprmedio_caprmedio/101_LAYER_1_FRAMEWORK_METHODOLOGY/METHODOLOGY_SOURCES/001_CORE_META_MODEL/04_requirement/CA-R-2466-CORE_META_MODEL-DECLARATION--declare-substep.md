---
atom_id: CA-R-2466
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Atom/(.Role := Operations)/Substep
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---

## Summary

Declare Substep

## Claim

```CFEL
Atom/(.Role: Operations)/Substep;
Substep//{:1}((IS_CONTAINED_BY)) Step//;
Substep//{:1}((RUN)) Action//
```

## Semantics

A Substep is a leaf unit within a Step. It runs a reusable Action.
