---
atom_id: CA-R-2420
ref_id: CA-R-2420
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_EXECUTED_BY
tier: 1
status: Active
version: 5
updated_at: 2026-11-03 20:00:05 +0400
carrier_destination:
  file:
    name: CA-R-2420-CORE_META_MODEL-DECLARATION--define-is-executed-by-relation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2420-CORE_META_MODEL-DECLARATION--define-is-executed-by-relation.md
  source_atom_id: CA-R-2420
  source_atom_revision: 5
  source_sha256: b209dda0645127dd620ed5d35d709bb5312391eb27866ae0c836fe646f44247b
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
