---
atom_id: CA-R-2525
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Package
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---

## Summary

Declare Package

## Claim

```CFEL
Package >| (Container == yes);
Package//{:0..1}((IS_CONTAINED_BY)) Package//;
Package//{:0+}((CONTAINS)) Package//;
IF (Package//$package not in (Package/Implementation//))
THEN ($package {==1}((IS_CONTAINED_BY)) Package//);
Package ((NARROWER_THAN)) @Continuant
```

## Semantics

A logical collection of implementation and documentation parts.
