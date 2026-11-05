---
atom_id: CA-R-2609
ref_id: CA-R-2609
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL<+Operator//NamedRelationDirection
tier: 3
status: Active
version: 2
updated_at: 2026-11-03 20:00:05 +0400
carrier_destination:
  file:
    name: CA-R-2609-CORE_META_MODEL-DECLARATION--declare-cfel-operator-named-relation-direction.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2609-CORE_META_MODEL-DECLARATION--declare-cfel-operator-named-relation-direction.md
  source_atom_id: CA-R-2609
  source_atom_revision: 2
  source_sha256: e05682ea5a790e9f9437cb15708ec2d8ad3d3ac493f1e126ce6d082009d5ba80
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare CFEL operator named Relation direction

## Claim

### Prose Claim

`Source ((RELATION)) Target` is forward and `Target <((RELATION)) Source` is reverse writing of the same canonical Relation fact. Counts stay on written endpoints; reverse normalization swaps canonical Host/Target and count slots. The declared Relation name is matched exactly. This CFEL operator is distinct from the named graph Relation. It grants no inverse permission and creates no second stored fact.
### Formal Claim

```CFEL
# model
Operator//NamedRelationDirection == "((RELATION)) / <((RELATION))"
```

