---
atom_id: CA-R-2620
role: Requirement
form: Declaration
status: Active
version: 1
updated_at: 2026-11-02 07:49:21 +0400
current_scope_unit: CORE_META_MODEL
tier: 3
subjects:
  active: CFEL <+ Relation//HAS_NARROWER
relations: {}
---

## Summary

Declare HAS_NARROWER

## Claim

A declared kind has a narrower kind. HAS_NARROWER is the derived inverse of NARROWER_THAN. It expresses the same fact and is not authored separately.

```CFEL
$broader ((HAS_NARROWER)) $narrower;
((NARROWER_THAN)) ((HAS_INVERSE)) ((HAS_NARROWER))

((HAS_NARROWER)) >| Derivation == Derived;
((HAS_NARROWER)) ((IS_DERIVED_RELATION_OF)) ((NARROWER_THAN))
```

## Semantics

The endpoints are declared kinds supporting narrowing; a Property does not narrow.


Forward `Host ((HAS_NARROWER)) Target` and reverse `Target <((HAS_NARROWER)) Host` are views of the same Relation fact.
HAS_NARROWER relates broader declared kind to narrower declared kind. It is the derived inverse of NARROWER_THAN; it does not add a separately authored fact.

