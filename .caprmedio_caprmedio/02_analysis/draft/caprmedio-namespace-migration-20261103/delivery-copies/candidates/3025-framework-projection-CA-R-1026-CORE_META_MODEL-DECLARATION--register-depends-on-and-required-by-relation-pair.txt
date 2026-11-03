---
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//depends_on
  passive:
  - CAPRMEDIO <+ MODEL <+ CFEL <+ Relation
  - CAPRMEDIO <+ MODEL <+ Term//Artifact
  - CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//required_by
version: 32
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
atom_id: CA-R-1026
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1026-CORE_META_MODEL-DECLARATION--register-depends-on-and-required-by-relation-pair.md
  source_atom_id: CA-R-1026
  source_atom_revision: 32
  source_sha256: 0bf456c661f73c353891d315b48231bf84da00049e350e92a0afb82e6ed15e70
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Register depends_on and required_by relation pair

## Claim scope

the `depends_on` **and** `required_by` relation pair.

## Claim

`depends_on` **means** a direct dependency-ordering relation from a dependent Artifact **to** its prerequisite Artifact, with `required_by` as its inverse-derived view. Plan start dependencies use the Plan Graph's `BLOCKS` under CA-R-1580 instead; this Relation Kind **must not** duplicate that scheduling fact.

```CFEL
((depends_on)) ((HAS_INVERSE)) ((required_by));

((depends_on)) >| Derivation == Direct;

$dependent ((depends_on)) $prerequisite
```

## Semantics



Both endpoints are Artifacts: the Host is dependent and the Target is its prerequisite.
Forward `Host ((depends_on)) Target` and reverse `Target <((depends_on)) Host` are views of the same Relation fact.
depends_on relates dependent Artifact to prerequisite Artifact.

