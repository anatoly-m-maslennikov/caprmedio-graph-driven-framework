---
atom_id: CA-R-2526
ref_id: CA-R-2526
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit.ID
tier: 3
status: Active
version: 4
updated_at: 2026-11-04 05:21:15 +0400
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2526-CORE_META_MODEL-DECLARATION--declare-scope-unit-id.md
  source_atom_id: CA-R-2526
  source_atom_revision: 4
  source_sha256: afda96e5c9c47cf3aa89e0223531608d9fee9f2120325bb73b3b3b856efe6ee1
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Scope Unit ID

## Claim

### Formal Claim

```CFEL
# model
Scope Unit.ID:: [string]{::0..1};

Scope Unit.ID.*[]{::0};

# instances
IF (Scope Unit//$unit not in (Scope Unit/Project//$scope_unit))
THEN ($unit.ID{::1})
```

## Semantics

A non-root Scope Unit keeps its ID through moves and renames. The ID distinguishes those operations from removing that Scope Unit. The Project root has no Scope Unit ID because it cannot be moved or renamed through Scope Unit operations.
