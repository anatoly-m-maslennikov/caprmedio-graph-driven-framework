---
atom_id: CA-R-2418
current_scope_unit: CORE_META_MODEL
status: Active
tier: 1
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//IS_CARRIED_BY
relations: {}
version: 4
updated_at: 2026-11-02 08:06:47 +0400
claim_target_scope_unit: CORE_META_MODEL
role: Requirement
form: Declaration
---
## Summary

Define IS_CARRIED_BY Relation

## Claim

IS_CARRIED_BY is the declared inverse of CARRIES; its full Carrier-binding meaning remains in CA-R-1993. No independently stored reverse fact is introduced.

```CFEL
((CARRIES)) ((HAS_INVERSE)) ((IS_CARRIED_BY));

((IS_CARRIED_BY)) >| Derivation == Derived;
((IS_CARRIED_BY)) ((IS_DERIVED_RELATION_OF)) ((CARRIES));

$represented_entity ((IS_CARRIED_BY)) Carrier//
```

## Semantics



The Host is the non-ephemeral Entity stored or represented by the Carrier.
Forward `Host ((IS_CARRIED_BY)) Target` and reverse `Target <((IS_CARRIED_BY)) Host` are views of the same Relation fact.
IS_CARRIED_BY relates non-ephemeral Entity to Carrier. It is the derived inverse of CARRIES; it does not add a separately authored fact.

