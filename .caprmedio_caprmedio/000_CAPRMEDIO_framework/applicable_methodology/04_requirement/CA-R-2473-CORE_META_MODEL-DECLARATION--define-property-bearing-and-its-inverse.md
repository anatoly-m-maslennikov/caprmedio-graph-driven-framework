---
atom_id: CA-R-2473
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_PROPERTY_OF
version: 5
updated_at: 2026-11-03 20:00:05 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2473-CORE_META_MODEL-DECLARATION--define-property-bearing-and-its-inverse.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2473-CORE_META_MODEL-DECLARATION--define-property-bearing-and-its-inverse.md
  source_atom_id: CA-R-2473
  source_atom_revision: 5
  source_sha256: e9e6ef725504569522386ec508820391a97df534812c1a8557916cc11d1b5b00
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define Property bearing and its inverse

## Claim

### Formal Claim

```CFEL
# model
$property ((IS_PROPERTY_OF)) $bearer;

Relation//IS_PROPERTY_OF ((HAS_INVERSE)) Relation//HAS_PROPERTY;

alias(Relation//IS_PROPERTY_OF) == ".";

Relation//IS_PROPERTY_OF ((HAS_CLASSIFICATION)) Derivation == Direct
```

### Prose Claim

IS_PROPERTY_OF directs a Property to exactly one immediate bearer. HAS_PROPERTY is its derived inverse. The bearer relation is acyclic. `Bearer.Property` addresses the Property.

A Property has exactly one immediate bearer; the bearer may be any applicable declared model Entity or instance.

Forward `Host ((IS_PROPERTY_OF)) Target` and reverse `Target <((IS_PROPERTY_OF)) Host` are views of the same Relation fact.
In `X.Y`, Y IS_PROPERTY_OF X; traversal runs from bearer to Property.
IS_PROPERTY_OF relates Property to immediate bearer.
