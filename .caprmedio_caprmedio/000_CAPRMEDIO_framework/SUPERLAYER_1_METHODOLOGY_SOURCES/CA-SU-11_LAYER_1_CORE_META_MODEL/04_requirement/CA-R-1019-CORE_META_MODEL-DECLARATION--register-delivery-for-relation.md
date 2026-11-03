---
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//delivery_for
  passive:
  - CAPRMEDIO <+ MODEL <+ CFEL > Relation
version: 29
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
atom_id: CA-R-1019
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Declaration
---
## Summary

Register delivery_for relation

## Claim scope

`delivery_for` relations.

## Claim

`delivery_for` **means** the direct relation from a Delivery Atom to the Atom
that the Delivery realizes.

```CFEL
((delivery_for)) >| Derivation == Direct;

Atom/(.Role: Delivery)// ((delivery_for)) Atom//
```

## Semantics


Forward `Host ((delivery_for)) Target` and reverse `Target <((delivery_for)) Host` are views of the same Relation fact.
delivery_for relates Delivery Atom to realized Atom.

