---
subjects:
  active: CFEL <+ Relation//rationale_for
  passive:
  - CFEL > Relation
version: 30
updated_at: 2026-11-02 07:52:54 +0400
relations: {}
atom_id: CA-R-1016
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Declaration
---
## Summary

Register rationale_for relation

## Claim scope

Rationale For Relation.

## Claim

`rationale_for` **means** the direct relation from a Rationale Analysis Atom
to the Atom that it explains.

```CFEL
((rationale_for)) >| Derivation == Direct;

Atom/(.Role: Analysis)/(.Form: Rationale)// ((rationale_for)) Atom//
```

## Semantics


Forward `Host ((rationale_for)) Target` and reverse `Target <((rationale_for)) Host` are views of the same Relation fact.
rationale_for relates Rationale Analysis Atom to explained Atom.

