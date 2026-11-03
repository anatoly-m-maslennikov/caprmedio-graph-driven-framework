---
atom_id: CA-R-2619
role: Requirement
form: Declaration
status: Active
version: 1
updated_at: 2026-11-02 08:06:47 +0400
current_scope_unit: CORE_META_MODEL
tier: 3
subjects:
  active: CFEL <+ Relation//HAS_INSTANCE
relations: {}
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2619-CORE_META_MODEL-DECLARATION--declare-has-instance.md
  source_atom_id: CA-R-2619
  source_atom_revision: 1
  source_sha256: aa5e983e23522d6c877f2b085a2b3efbddbd306bac4f6948b1115f5e3e44131f
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare HAS_INSTANCE

## Claim

A declared kind has an instance of that kind. HAS_INSTANCE is the derived inverse of INSTANCE_OF. It expresses the same fact and is not authored separately.

```CFEL
$kind ((HAS_INSTANCE)) $instance;
((INSTANCE_OF)) ((HAS_INVERSE)) ((HAS_INSTANCE));

((HAS_INSTANCE)) >| Derivation == Derived;
((HAS_INSTANCE)) ((IS_DERIVED_RELATION_OF)) ((INSTANCE_OF))
```

## Semantics

The Target is an instance of the Host declared kind; a Property kind is not independently instantiated.


Forward `Host ((HAS_INSTANCE)) Target` and reverse `Target <((HAS_INSTANCE)) Host` are views of the same Relation fact.
HAS_INSTANCE relates declared kind to instance of that kind. It is the derived inverse of INSTANCE_OF; it does not add a separately authored fact.

