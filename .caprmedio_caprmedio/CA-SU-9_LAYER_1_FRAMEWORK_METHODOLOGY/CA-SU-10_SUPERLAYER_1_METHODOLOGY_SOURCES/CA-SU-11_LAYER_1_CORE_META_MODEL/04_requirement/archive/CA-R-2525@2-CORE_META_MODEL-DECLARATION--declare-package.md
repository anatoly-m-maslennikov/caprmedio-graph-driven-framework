---
atom_id: CA-R-2525
ref_id: CA-R-2525@2
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Package
tier: 3
status: Archived
version: 2
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-2525@2-CORE_META_MODEL-DECLARATION--declare-package.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/archive
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
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
Package//$package_2{::0..1}((IS_CONTAINED_BY)) Package//$package_3;

Package//$package_4{::0+}((CONTAINS)) Package//$package_5;

IF (Package//$package not in (Package/Implementation//$package_6))
THEN ($package {==1}((IS_CONTAINED_BY)) Package//$package_7);
```

## Semantics

A logical collection of implementation and documentation parts.
