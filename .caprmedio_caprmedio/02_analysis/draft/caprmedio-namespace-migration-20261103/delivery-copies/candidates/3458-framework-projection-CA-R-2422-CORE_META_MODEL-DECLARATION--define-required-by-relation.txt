---
atom_id: CA-R-2422
current_scope_unit: CORE_META_MODEL
status: Active
tier: 1
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//required_by
relations: {}
version: 4
updated_at: 2026-11-02 08:06:47 +0400
claim_target_scope_unit: CORE_META_MODEL
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2422-CORE_META_MODEL-DECLARATION--define-required-by-relation.md
  source_atom_id: CA-R-2422
  source_atom_revision: 4
  source_sha256: 0fda122dcb0307249e1c25e66aed6bf5a776cefcbb9c1bcb1b860d85a1b10e7d
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define required_by Relation

## Claim

required_by is the inverse-derived view of depends_on; its full dependency-ordering meaning remains in CA-R-1026. No independently stored reverse fact is introduced.

```CFEL
((depends_on)) ((HAS_INVERSE)) ((required_by));

((required_by)) >| Derivation == Derived;
((required_by)) ((IS_DERIVED_RELATION_OF)) ((depends_on));

$prerequisite ((required_by)) $dependent
```

## Semantics



Both endpoints are Artifacts: the Host is the prerequisite and the Target is dependent.
Forward `Host ((required_by)) Target` and reverse `Target <((required_by)) Host` are views of the same Relation fact.
required_by relates prerequisite Artifact to dependent Artifact. It is the derived inverse of depends_on; it does not add a separately authored fact.

