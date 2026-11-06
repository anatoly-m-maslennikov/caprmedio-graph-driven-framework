---
atom_id: CA-R-1021
ref_id: CA-R-1021
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//evidence_for
  dependencies:
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
tier: 1
status: Active
version: 33
updated_at: 2026-11-04 22:00:28 +0400
carrier_destination:
  file:
    name: CA-R-1021-DECLARATION--register-evidence-for-relation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1021-CORE_META_MODEL-DECLARATION--register-evidence-for-relation.md
  source_atom_id: CA-R-1021
  source_atom_revision: 33
  source_sha256: 94da98174b6c69d36c0d90800cd5aaa3bfd0957259c903670307bbdc24cfb1bd
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Register evidence_for relation

## Claim

### Prose Claim

evidence_for is the direct Relation owned by an evidence Carrier. The Host is that evidence Carrier and each tuple targets the Evaluation or Implementation Carrier it supports.

### Formal Claim

```CFEL
# model
Relation//evidence_for ((HAS_CLASSIFICATION)) Derivation == Direct;

# instances
Carrier//$evidence_carrier ((evidence_for)) Carrier//$supported_carrier
```

