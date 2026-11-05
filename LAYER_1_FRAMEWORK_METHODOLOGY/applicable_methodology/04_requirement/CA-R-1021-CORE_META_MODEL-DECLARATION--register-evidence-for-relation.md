---
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//evidence_for
  passive:
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
version: 33
updated_at: 2026-11-04 22:00:28 +0400
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
atom_id: CA-R-1021
status: Active
tier: 1
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-1021-CORE_META_MODEL-DECLARATION--register-evidence-for-relation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1021-CORE_META_MODEL-DECLARATION--register-evidence-for-relation.md
  source_atom_id: CA-R-1021
  source_atom_revision: 33
  source_sha256: 18c323b0bc5d01d2a45f6eb30c4ca4bdd656d5c2e5841381ab39e903b333158b
  original_relations_sha256: e367927d209b7bdecd9da53dd0dc693193d074370738c97b4bc15988d6240196
---
## Summary

Register evidence_for relation

## Claim

### Formal Claim

```CFEL
# model
Relation//evidence_for ((HAS_CLASSIFICATION)) Derivation == Direct;

# instances
Carrier//$evidence_carrier ((evidence_for)) Carrier//$supported_carrier
```

### Prose Claim

evidence_for is the direct Relation owned by an evidence Carrier. The Host is that evidence Carrier and each tuple targets the Evaluation or Implementation Carrier it supports.

