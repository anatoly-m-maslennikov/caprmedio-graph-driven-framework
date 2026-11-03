---
atom_id: CA-R-2478
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CFEL <+ Relation//IS_CONTAINED_BY
version: 4
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2478-CORE_META_MODEL-DECLARATION--define-composition-and-its-inverse.md
  source_atom_id: CA-R-2478
  source_atom_revision: 4
  source_sha256: 339e23481cdadae59b549e2f26a05742ee66e96a9977f50b7b2ff33bea06530b
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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

