---
atom_id: CA-R-2523
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Scope Unit
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2523-CORE_META_MODEL-DECLARATION--declare-scope-unit.md
  source_atom_id: CA-R-2523
  source_atom_revision: 2
  source_sha256: 3cab1b8e346b78c27598d4d4a443ac089f39fc310eef6c5e9e654f74c0bae868
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare Scope Unit

## Claim

```CFEL
Scope Unit >| (Container == yes);
Scope Unit//{:0..1}((IS_CONTAINED_BY)) Scope Unit//;
Scope Unit//{:0+}((CONTAINS)) Scope Unit//;
IF (Scope Unit//$unit not in (Scope Unit/Project//))
THEN ($unit {==1}((IS_CONTAINED_BY)) Scope Unit//);
Scope Unit ((NARROWER_THAN)) @Continuant
```

## Semantics

A Scope Unit defines a boundary of responsibility for Atoms.
