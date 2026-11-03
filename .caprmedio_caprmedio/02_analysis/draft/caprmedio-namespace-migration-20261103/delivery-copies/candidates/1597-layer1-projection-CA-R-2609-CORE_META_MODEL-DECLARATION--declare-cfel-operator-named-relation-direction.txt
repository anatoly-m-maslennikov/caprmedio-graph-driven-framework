---
atom_id: CA-R-2609
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL<+Operator//NamedRelationDirection
version: 1
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2609-CORE_META_MODEL-DECLARATION--declare-cfel-operator-named-relation-direction.md
  source_atom_id: CA-R-2609
  source_atom_revision: 1
  source_sha256: 0d3b96eec0e73c08a411282c23f8e2419625049507e4bd68d1d9f880e8252b63
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare CFEL operator named Relation direction

## Claim

```CFEL
@Operator//NamedRelationDirection == "((RELATION)) / <((RELATION))"
```

## Semantics

`Source ((RELATION)) Target` is forward and `Target <((RELATION)) Source`
is reverse for the same canonical Relation fact. Counts remain on written
endpoints; reverse normalization swaps canonical Source/Target and count slots.
This notation neither grants an inverse Relation nor makes field materialization
a derived Relation.
