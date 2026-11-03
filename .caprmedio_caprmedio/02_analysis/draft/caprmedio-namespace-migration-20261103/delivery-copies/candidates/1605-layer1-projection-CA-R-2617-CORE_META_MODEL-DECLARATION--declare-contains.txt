---
atom_id: CA-R-2617
role: Requirement
form: Declaration
status: Active
version: 1
updated_at: 2026-11-02 08:06:47 +0400
current_scope_unit: CORE_META_MODEL
tier: 3
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//CONTAINS
relations: {}
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2617-CORE_META_MODEL-DECLARATION--declare-contains.md
  source_atom_id: CA-R-2617
  source_atom_revision: 1
  source_sha256: 0200e72c654e701c21b0ca82e2cb8f02867a434703df641a483b7ce285fe4fc8
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare CONTAINS

## Claim

A Container contains the directly contained Entity or instance. CONTAINS is the derived inverse of IS_CONTAINED_BY. It expresses the same fact and is not authored separately.

```CFEL
$container ((CONTAINS)) $part;
((IS_CONTAINED_BY)) ((HAS_INVERSE)) ((CONTAINS));

((CONTAINS)) == <+;

((CONTAINS)) >| Derivation == Derived;
((CONTAINS)) ((IS_DERIVED_RELATION_OF)) ((IS_CONTAINED_BY))
```

## Semantics

The Host is the immediate Container of the Target and must have the classification `Container = yes`.

Forward `Host ((CONTAINS)) Target` and reverse `Target <((CONTAINS)) Host` are views of the same Relation fact.

CONTAINS relates Container to immediate contained Entity or instance. It is the derived inverse of IS_CONTAINED_BY; it does not add a separately authored fact.
