---
atom_id: CA-R-970308631
ref_id: CA-R-970308631
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Package/Project Package
tier: 3
status: Active
version: 1
updated_at: 2026-11-10 14:38:45 +0400
carrier_destination:
  file:
    name: CA-R-970308631-CORE_META_MODEL-DECLARATION--declare-project-package.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
relations:
  is_replacement_for:
  - CA-R-2553
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-970308631-CORE_META_MODEL-DECLARATION--declare-project-package.md
  source_atom_id: CA-R-970308631
  source_atom_revision: 1
  source_sha256: 901289665cf1cac3f7a847776f5024db89ed9a3d62c5bb67acd6ab0d20669b6f
  original_relations_sha256: db393ca5c05c09d7410fed3bb77c55fea66a2bc46986cfa5585536b1fae282a7
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
