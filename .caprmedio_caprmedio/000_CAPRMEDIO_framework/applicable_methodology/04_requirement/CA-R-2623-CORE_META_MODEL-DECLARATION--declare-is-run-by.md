---
atom_id: CA-R-2623
role: Requirement
form: Declaration
status: Active
version: 4
updated_at: 2026-11-03 20:00:05 +0400
current_scope_unit: CORE_META_MODEL
tier: 3
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_RUN_BY
relations: {}
carrier_destination:
  file:
    name: CA-R-2623-CORE_META_MODEL-DECLARATION--declare-is-run-by.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2623-CORE_META_MODEL-DECLARATION--declare-is-run-by.md
  source_atom_id: CA-R-2623
  source_atom_revision: 4
  source_sha256: dd540f1c2fd04b4826443a96daa6f7e190853ecd8645ad1a369d85a3744a2fc6
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare IS_RUN_BY

## Claim

### Formal Claim

```CFEL
# model
Relation//IS_RUN_BY <((HAS_INVERSE)) Relation//RUNS
```
