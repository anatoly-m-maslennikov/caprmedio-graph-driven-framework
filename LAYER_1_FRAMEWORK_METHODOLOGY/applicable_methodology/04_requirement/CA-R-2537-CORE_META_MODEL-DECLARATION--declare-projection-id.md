---
atom_id: CA-R-2537
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Projection.ID
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2537-CORE_META_MODEL-DECLARATION--declare-projection-id.md
  source_atom_id: CA-R-2537
  source_atom_revision: 2
  source_sha256: 6af76cf726181b5e6ab9f4d19783aef373f443454d753d94d2e07d284a2dfd52
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Projection.ID

## Claim

```CFEL
Projection.ID{:1}: [string]{:1};
Projection.ID.*[]{:0};
DETERMINES(Projection//, (.Form, .Source.Named Selection), (.ID));
DETERMINES(Projection//, (.ID), (.Form, .Source.Named Selection))
```
