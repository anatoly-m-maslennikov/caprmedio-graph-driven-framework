---
atom_id: CA-R-970308631
ref_id: CA-R-970308631@1
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Package/Project Package
tier: 3
status: Archived
version: 1
updated_at: 2026-11-10 14:38:45 +0400
carrier_destination:
  file:
    name: CA-R-970308631@1-CORE_META_MODEL-DECLARATION--declare-project-package.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
relations:
  is_replacement_for:
  - CA-R-2553
---

## Summary

Declare Project Package

## Claim

### Formal Claim

```CFEL
# model
Package/Project Package;

# instances
Package/Project Package//$package{::1};

Package/Project Package//$package_2 {::0}((IS_CONTAINED_BY)) Package//$package_3
```

## Semantics

The Project Package is the root Package of a Project's implementation.
