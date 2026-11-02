---
subjects:
  active: CFEL <+ Relation//concern_about
  passive:
  - CFEL > Relation
version: 31
updated_at: 2026-11-02 07:49:21 +0400
relations: {}
atom_id: CA-R-1022
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Declaration
---
## Summary

Register concern_about relation

## Claim scope

`concern_about` relations.

## Claim

`concern_about` **means** the direct relation from a Concern Atom to the
governed entity that it concerns.

```CFEL
((concern_about)) >| Derivation == Direct

Atom/(.Role: Concern)// ((concern_about)) $governed
```

## Semantics



The Host is a Concern Atom; the governed target is the Entity concerned.
Forward `Host ((concern_about)) Target` and reverse `Target <((concern_about)) Host` are views of the same Relation fact.
concern_about relates Concern Atom to governed entity concerned.

## Details

Endpoint admission is an Atom Entity Definition concern, not Relation Definition
metadata.
