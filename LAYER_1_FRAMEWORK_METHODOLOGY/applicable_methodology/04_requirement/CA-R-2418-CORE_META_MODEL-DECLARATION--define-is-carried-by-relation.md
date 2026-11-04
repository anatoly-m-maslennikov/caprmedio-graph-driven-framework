---
atom_id: CA-R-2418
current_scope_unit: CORE_META_MODEL
status: Active
tier: 1
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_CARRIED_BY
relations: {}
version: 5
updated_at: 2026-11-03 20:00:05 +0400
claim_target_scope_unit: CORE_META_MODEL
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2418-CORE_META_MODEL-DECLARATION--define-is-carried-by-relation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2418-CORE_META_MODEL-DECLARATION--define-is-carried-by-relation.md
  source_atom_id: CA-R-2418
  source_atom_revision: 5
  source_sha256: 4944f3098c5c6d1e4962ea88f6424cb1df23abcf0810e4c93cdc6d0f7f2d27ca
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define IS_CARRIED_BY Relation

## Claim

### Formal Claim

```CFEL
# model
Relation//IS_CARRIED_BY <((HAS_INVERSE)) Relation//CARRIES
```
