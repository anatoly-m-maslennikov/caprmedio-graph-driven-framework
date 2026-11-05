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

### Formal Claim

```CFEL
# model
Package >| (Container == yes);

Package ((NARROWER_THAN)) Continuant;

# instances
Package//$package_2{:0..1}((IS_CONTAINED_BY)) Package//$package_3;

Package//$package_4{:0+}((CONTAINS)) Package//$package_5;

IF (Package//$package not in (Package/Implementation//$package_6))
THEN ($package {==1}((IS_CONTAINED_BY)) Package//$package_7);
```

## Semantics

A logical collection of implementation and documentation parts.
