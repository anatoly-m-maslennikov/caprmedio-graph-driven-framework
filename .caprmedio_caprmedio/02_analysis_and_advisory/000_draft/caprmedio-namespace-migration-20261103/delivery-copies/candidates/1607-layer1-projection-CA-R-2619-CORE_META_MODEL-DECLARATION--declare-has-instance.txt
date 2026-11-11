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
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//HAS_INSTANCE
relations: {}
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2619-CORE_META_MODEL-DECLARATION--declare-has-instance.md
  source_atom_id: CA-R-2619
  source_atom_revision: 1
  source_sha256: 8b546e2f6bb434e5fad63ee7fe8176e6036be8535d78878cdc1743f703a089df
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

