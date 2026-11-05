---
atom_id: CA-R-2417
current_scope_unit: CORE_META_MODEL
status: Active
tier: 1
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//HAS_EXECUTION
relations: {}
version: 5
updated_at: 2026-11-03 20:00:05 +0400
claim_target_scope_unit: CORE_META_MODEL
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2417-CORE_META_MODEL-DECLARATION--define-has-execution-relation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2417-CORE_META_MODEL-DECLARATION--define-has-execution-relation.md
  source_atom_id: CA-R-2417
  source_atom_revision: 5
  source_sha256: e50b96e2a066c11c7deee1f31ef85197b74d09aaa93c12579648e7c9ef8bd691
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define HAS_EXECUTION Relation

## Claim

### Formal Claim

```CFEL
# model
Relation//HAS_EXECUTION <((HAS_INVERSE)) Relation//IS_EXECUTION_OF
```
