---
atom_id: CA-R-2621
role: Requirement
form: Declaration
status: Active
version: 1
updated_at: 2026-11-02 08:06:47 +0400
current_scope_unit: CORE_META_MODEL
tier: 3
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//HAS_PROPERTY
relations: {}
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2621-CORE_META_MODEL-DECLARATION--declare-has-property.md
  source_atom_id: CA-R-2621
  source_atom_revision: 1
  source_sha256: c59bd36ff4ca5a1558a25b13735fd56e1178bb9993f88da655cdc75de365a9e1
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare HAS_PROPERTY

## Claim

A bearer has its dependent Property. HAS_PROPERTY is the derived inverse of IS_PROPERTY_OF. It expresses the same fact and is not authored separately.

```CFEL
$bearer ((HAS_PROPERTY)) $property;
((IS_PROPERTY_OF)) ((HAS_INVERSE)) ((HAS_PROPERTY));

((HAS_PROPERTY)) >| Derivation == Derived;
((HAS_PROPERTY)) ((IS_DERIVED_RELATION_OF)) ((IS_PROPERTY_OF))
```

## Semantics

The Target is a Property borne directly by the Host.


Forward `Host ((HAS_PROPERTY)) Target` and reverse `Target <((HAS_PROPERTY)) Host` are views of the same Relation fact.
HAS_PROPERTY relates Node or Property to dependent Property. It is the derived inverse of IS_PROPERTY_OF; it does not add a separately authored fact.

