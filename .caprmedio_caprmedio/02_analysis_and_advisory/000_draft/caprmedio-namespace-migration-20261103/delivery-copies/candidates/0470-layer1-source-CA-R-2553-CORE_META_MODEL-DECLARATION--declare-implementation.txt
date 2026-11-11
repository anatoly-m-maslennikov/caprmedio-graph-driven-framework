---
atom_id: CA-R-2553
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Package/Implementation
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---

## Summary

Declare Implementation

## Claim

```CFEL
Package/Implementation;
Package/Implementation//{:1};
Package/Implementation// {:0}((IS_CONTAINED_BY)) Package//
```

## Semantics

The root Package of a Project's implementation.
