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
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2418-CORE_META_MODEL-DECLARATION--define-is-carried-by-relation.md
  source_atom_id: CA-R-2418
  source_atom_revision: 4
  source_sha256: 3f187b8172b8d400aa205af6090fc56da0afec7d407662c3377a2d6cfbaac613
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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

