---
atom_id: CA-R-2473
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//IS_PROPERTY_OF
version: 4
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2473-CORE_META_MODEL-DECLARATION--define-property-bearing-and-its-inverse.md
  source_atom_id: CA-R-2473
  source_atom_revision: 4
  source_sha256: 61ffa3489068dd8542d647b676b93f76dda6a0fddfd35256f52e47f9bedfbd05
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define Property bearing and its inverse

## Claim

IS_PROPERTY_OF directs a Property to exactly one immediate bearer. HAS_PROPERTY is its derived inverse. The bearer relation is acyclic. `Bearer.Property` addresses the Property.

```CFEL
$property ((IS_PROPERTY_OF)) $bearer;
((IS_PROPERTY_OF)) ((HAS_INVERSE)) ((HAS_PROPERTY));

((IS_PROPERTY_OF)) == .;
((IS_PROPERTY_OF)) >| Derivation == Direct
```

## Semantics

A Property has exactly one immediate bearer; the bearer may be any applicable declared model Entity or instance.



Forward `Host ((IS_PROPERTY_OF)) Target` and reverse `Target <((IS_PROPERTY_OF)) Host` are views of the same Relation fact.
In `X.Y`, Y IS_PROPERTY_OF X; traversal runs from bearer to Property.
IS_PROPERTY_OF relates Property to immediate bearer.

