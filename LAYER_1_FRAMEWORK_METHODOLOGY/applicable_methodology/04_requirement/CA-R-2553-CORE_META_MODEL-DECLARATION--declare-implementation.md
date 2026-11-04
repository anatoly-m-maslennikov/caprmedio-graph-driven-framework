---
atom_id: CA-R-2553
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Package/Implementation
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2553-CORE_META_MODEL-DECLARATION--declare-implementation.md
  source_atom_id: CA-R-2553
  source_atom_revision: 2
  source_sha256: 95277e91faeffdfa209190a16070768bfd3e4690b04695c543d0b30f124dd090
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare Implementation

## Claim

### Formal Claim

```CFEL
# model
Package/Implementation;

# instances
Package/Implementation//$package{:1};

Package/Implementation//$package_2 {:0}((IS_CONTAINED_BY)) Package//$package_3
```

## Semantics

The root Package of a Project's implementation.
