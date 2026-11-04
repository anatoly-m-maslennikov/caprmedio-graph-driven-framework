---
atom_id: CA-R-2420
current_scope_unit: CORE_META_MODEL
status: Active
tier: 1
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_EXECUTED_BY
relations: {}
version: 5
updated_at: 2026-11-03 20:00:05 +0400
claim_target_scope_unit: CORE_META_MODEL
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2420-CORE_META_MODEL-DECLARATION--define-is-executed-by-relation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2420-CORE_META_MODEL-DECLARATION--define-is-executed-by-relation.md
  source_atom_id: CA-R-2420
  source_atom_revision: 5
  source_sha256: 52e09f067858fcaa9c26bfd100227b9c7866058482054e0fca93331cdc238263
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define IS_EXECUTED_BY Relation

## Claim

### Formal Claim

```CFEL
# model
Relation//IS_EXECUTED_BY <((HAS_INVERSE)) Relation//EXECUTES
```
