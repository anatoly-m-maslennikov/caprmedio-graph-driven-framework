---
atom_id: CA-R-2478
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//IS_CONTAINED_BY
version: 4
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---
## Summary

Define composition and its inverse

## Claim

IS_CONTAINED_BY relates a contained declared Entity or instance to its immediate Container. Containment does not imply narrowing or inheritance.

```CFEL
$part ((IS_CONTAINED_BY)) $container;
((IS_CONTAINED_BY)) ((HAS_INVERSE)) ((CONTAINS));

((IS_CONTAINED_BY)) == +>;

((IS_CONTAINED_BY)) >| Derivation == Direct
```

## Semantics

The Target is the immediate Container of the Host and must have the classification `Container = yes`; containment does not imply narrowing or inheritance.


Forward `Host ((IS_CONTAINED_BY)) Target` and reverse `Target <((IS_CONTAINED_BY)) Host` are views of the same Relation fact.
IS_CONTAINED_BY relates contained declared Entity or instance to immediate Container.

