---
atom_id: CA-R-2619
role: Requirement
form: Declaration
status: Active
version: 2
updated_at: 2026-11-03 20:00:05 +0400
current_scope_unit: CORE_META_MODEL
tier: 3
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//HAS_INSTANCE
relations: {}
carrier_destination:
  file:
    name: CA-R-2619-CORE_META_MODEL-DECLARATION--declare-has-instance.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2619-CORE_META_MODEL-DECLARATION--declare-has-instance.md
  source_atom_id: CA-R-2619
  source_atom_revision: 2
  source_sha256: f8d8f828420b31bfedced5bbcd2eb9c51086c30b3b61e2d1cd8712f8bddb516b
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare HAS_INSTANCE

## Claim

### Formal Claim

```CFEL
# model
Relation//HAS_INSTANCE <((HAS_INVERSE)) Relation//INSTANCE_OF
```
