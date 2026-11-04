---
atom_id: CA-R-2422
current_scope_unit: CORE_META_MODEL
status: Active
tier: 1
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//required_by
relations: {}
version: 5
updated_at: 2026-11-03 20:00:05 +0400
claim_target_scope_unit: CORE_META_MODEL
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2422-CORE_META_MODEL-DECLARATION--define-required-by-relation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2422-CORE_META_MODEL-DECLARATION--define-required-by-relation.md
  source_atom_id: CA-R-2422
  source_atom_revision: 5
  source_sha256: 99a6c6ff6a56f1fa98a1ab141749ced037e9f0aa7cea75f92f1e5371b4875349
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define required_by Relation

## Claim

### Formal Claim

```CFEL
# model
Relation//required_by <((HAS_INVERSE)) Relation//depends_on
```
