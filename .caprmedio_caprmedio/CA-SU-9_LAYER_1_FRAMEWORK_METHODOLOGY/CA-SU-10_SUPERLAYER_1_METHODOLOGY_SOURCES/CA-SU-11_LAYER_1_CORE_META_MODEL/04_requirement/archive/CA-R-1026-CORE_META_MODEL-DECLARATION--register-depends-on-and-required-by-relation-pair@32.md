---
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//depends_on
  passive:
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
  - CAPRMEDIO_MODEL <+ Term//Artifact
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//required_by
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

