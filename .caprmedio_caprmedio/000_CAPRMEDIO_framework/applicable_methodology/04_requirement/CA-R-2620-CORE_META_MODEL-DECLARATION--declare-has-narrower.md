---
atom_id: CA-R-2620
role: Requirement
form: Declaration
status: Active
version: 1
updated_at: 2026-11-02 08:06:47 +0400
current_scope_unit: CORE_META_MODEL
tier: 3
subjects:
  active: CFEL <+ Relation//HAS_NARROWER
relations: {}
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2620-CORE_META_MODEL-DECLARATION--declare-has-narrower.md
  source_atom_id: CA-R-2620
  source_atom_revision: 1
  source_sha256: d56e36ed3e96f38f1bb5f97aa428625d909b425fd1ca3962bd30909f4f00c5d6
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare HAS_NARROWER

## Claim

A declared kind has a narrower kind. HAS_NARROWER is the derived inverse of NARROWER_THAN. It expresses the same fact and is not authored separately.

```CFEL
$broader ((HAS_NARROWER)) $narrower;
((NARROWER_THAN)) ((HAS_INVERSE)) ((HAS_NARROWER));

((HAS_NARROWER)) >| Derivation == Derived;
((HAS_NARROWER)) ((IS_DERIVED_RELATION_OF)) ((NARROWER_THAN))
```

## Semantics

The endpoints are declared kinds supporting narrowing; a Property does not narrow.


Forward `Host ((HAS_NARROWER)) Target` and reverse `Target <((HAS_NARROWER)) Host` are views of the same Relation fact.
HAS_NARROWER relates broader declared kind to narrower declared kind. It is the derived inverse of NARROWER_THAN; it does not add a separately authored fact.

