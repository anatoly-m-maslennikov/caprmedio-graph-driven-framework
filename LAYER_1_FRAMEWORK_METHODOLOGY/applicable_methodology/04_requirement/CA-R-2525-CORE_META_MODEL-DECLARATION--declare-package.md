---
atom_id: CA-R-2525
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Package
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2525-CORE_META_MODEL-DECLARATION--declare-package.md
  source_atom_id: CA-R-2525
  source_atom_revision: 2
  source_sha256: 988e5875532af265502c17ea5a5d8f1b1b1f826741c2f056c08f469f768ecc7d
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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
