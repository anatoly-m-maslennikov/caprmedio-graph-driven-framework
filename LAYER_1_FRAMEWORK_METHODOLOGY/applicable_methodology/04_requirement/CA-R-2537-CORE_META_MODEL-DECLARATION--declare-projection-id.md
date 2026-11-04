---
atom_id: CA-R-2537
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Projection.ID
version: 3
updated_at: 2026-11-04 07:51:19 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2537-CORE_META_MODEL-DECLARATION--declare-projection-id.md
  source_atom_id: CA-R-2537
  source_atom_revision: 3
  source_sha256: 4bf298a918f5f9fab0dcdbf6c143eb9e3e51b65f6af060e424173c0b6fc59022
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Projection.ID

## Claim

### Formal Claim

```CFEL
# model
Projection.ID{:1}: [string]{:1};

Projection.ID.*[]{:0};

# instances
DETERMINES(Projection//$projection, (.Form, .Scope Unit), (.ID));

DETERMINES(Projection//$projection_2, (.ID), (.Form, .Scope Unit))
```

