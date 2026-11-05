---
atom_id: CA-R-1026
ref_id: CA-R-1026
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//depends_on
  dependencies:
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
  - CAPRMEDIO_MODEL <+ Term//Artifact
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//required_by
tier: 1
status: Active
version: 33
updated_at: 2026-11-03 20:00:05 +0400
carrier_destination:
  file:
    name: CA-R-1026-CORE_META_MODEL-DECLARATION--register-depends-on-and-required-by-relation-pair.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Register depends_on and required_by relation pair

## Claim

### Prose Claim

#### Claim scope
the `depends_on` **and** `required_by` relation pair.

`depends_on` **means** a direct dependency-ordering relation from a dependent Artifact **to** its prerequisite Artifact, with `required_by` as its inverse-derived view. Plan start dependencies use the Plan Graph's `BLOCKS` under CA-R-1580 instead; this Relation Kind **must not** duplicate that scheduling fact.

Both endpoints are Artifacts: the Host is dependent and the Target is its prerequisite.
Forward `Host ((depends_on)) Target` and reverse `Target <((depends_on)) Host` are views of the same Relation fact.
depends_on relates dependent Artifact to prerequisite Artifact.
### Formal Claim

```CFEL
# model
Relation//depends_on ((HAS_INVERSE)) Relation//required_by;

Relation//depends_on ((HAS_CLASSIFICATION)) Derivation == Direct;

# instances
$dependent ((depends_on)) $prerequisite
```

