---
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//implementation_of
  passive:
  - CAPRMEDIO <+ MODEL <+ CFEL > Relation
version: 29
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
atom_id: CA-R-1020
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Declaration
---
## Summary

Register implementation_of relation

## Claim scope

the `implementation_of` direct relation owned by a governed Implementation carrier.

## Claim

`implementation_of` **means** the direct relation from an Implementation
carrier to the specification Atom that it implements.

```CFEL
((implementation_of)) >| Derivation == Direct;

$implementation_carrier ((implementation_of)) Atom//
```

## Semantics



The Host is an Implementation carrier; the target is the specification Atom it implements.
Forward `Host ((implementation_of)) Target` and reverse `Target <((implementation_of)) Host` are views of the same Relation fact.
implementation_of relates Implementation carrier to specification Atom.

