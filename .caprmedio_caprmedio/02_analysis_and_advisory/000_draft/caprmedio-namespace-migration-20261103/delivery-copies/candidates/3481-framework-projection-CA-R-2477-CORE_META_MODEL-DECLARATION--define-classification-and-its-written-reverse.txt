---
atom_id: CA-R-2477
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//HAS_CLASSIFICATION
version: 4
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2477-CORE_META_MODEL-DECLARATION--define-classification-and-its-written-reverse.md
  source_atom_id: CA-R-2477
  source_atom_revision: 4
  source_sha256: 3b16fc0af0c9662d00e5e2fb229c4fac81bd7f66c80b8f0a27c5858b41b406a1
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define classification and its written reverse

## Claim

HAS_CLASSIFICATION relates a declared Entity or instance to an applicable classification axis. `Entity >| Axis` and `Axis |< Entity` are opposite written views of the same fact. An axis is distinct from its value case.

```CFEL
$classified ((HAS_CLASSIFICATION)) $axis;

((HAS_CLASSIFICATION)) == >|;

((HAS_CLASSIFICATION)) >| Derivation == Direct
```

## Semantics

The Target is an applicable classification axis; the classified Entity may be a Relation or another declared Entity.


Forward `Host ((HAS_CLASSIFICATION)) Target` and reverse `Target <((HAS_CLASSIFICATION)) Host` are views of the same Relation fact.
HAS_CLASSIFICATION relates declared Entity or instance to applicable classification axis.

