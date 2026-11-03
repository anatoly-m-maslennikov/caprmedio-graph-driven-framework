---
atom_id: CA-R-2526
status: Active
subjects:
  active: Scope Unit.ID
version: 3
updated_at: 2026-11-02 19:17:40 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2526-CORE_META_MODEL-DECLARATION--declare-scope-unit-id.md
  source_atom_id: CA-R-2526
  source_atom_revision: 3
  source_sha256: bcbcd8b65f0612f4731269e7b7514d251ae8fd451b6a3ff943ca01c9429c32e4
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Scope Unit ID

## Claim

```CFEL
Scope Unit.ID{:0..1}: [string]{:1};
Scope Unit.ID.*[]{:0};
IF (Scope Unit//$unit not in (Scope Unit/Project//))
THEN ($unit.ID{:1})
```

## Semantics

A non-root Scope Unit keeps its ID through moves and renames. The ID distinguishes those operations from removing that Scope Unit. The Project root has no Scope Unit ID because it cannot be moved or renamed through Scope Unit operations.
