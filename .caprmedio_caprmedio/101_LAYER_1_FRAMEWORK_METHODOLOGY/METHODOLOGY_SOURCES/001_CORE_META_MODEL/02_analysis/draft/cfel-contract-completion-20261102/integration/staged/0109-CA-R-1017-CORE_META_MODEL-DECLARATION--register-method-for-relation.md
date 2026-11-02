---
subjects:
  active: CFEL <+ Relation//method_for
  passive:
  - CFEL > Relation
version: 30
updated_at: 2026-11-02 07:52:54 +0400
relations: {}
atom_id: CA-R-1017
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Declaration
---
## Summary

Register method_for relation

## Claim scope

Method For Relation.

## Claim

`method_for` **means** the direct relation from a Method Atom to the
Requirement Atom that the Method serves.

```CFEL
((method_for)) >| Derivation == Direct;

Atom/(.Role: Method)// ((method_for)) Atom/(.Role: Requirement)//
```

## Semantics


Forward `Host ((method_for)) Target` and reverse `Target <((method_for)) Host` are views of the same Relation fact.
method_for relates Method Atom to served Requirement Atom.

