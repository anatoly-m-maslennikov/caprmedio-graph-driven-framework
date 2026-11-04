---
atom_id: CA-R-2477
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//HAS_CLASSIFICATION
version: 5
updated_at: 2026-11-03 20:00:05 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2477-CORE_META_MODEL-DECLARATION--define-classification-and-its-written-reverse.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2477-CORE_META_MODEL-DECLARATION--define-classification-and-its-written-reverse.md
  source_atom_id: CA-R-2477
  source_atom_revision: 5
  source_sha256: e4b24cf8cabe401be72fde576c8d4694e8e72ca63ab18066c274a3c12da174af
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define classification and its written reverse

## Claim

### Formal Claim

```CFEL
# model
$classified ((HAS_CLASSIFICATION)) $axis;

alias(Relation//HAS_CLASSIFICATION) == ">|";

Relation//HAS_CLASSIFICATION ((HAS_CLASSIFICATION)) Derivation == Direct
```

### Prose Claim

HAS_CLASSIFICATION relates a declared Entity or instance to an applicable classification axis. `Entity >| Axis` and `Axis |< Entity` are opposite written views of the same fact. An axis is distinct from its value case.

The Target is an applicable classification axis; the classified Entity may be a Relation or another declared Entity.

Forward `Host ((HAS_CLASSIFICATION)) Target` and reverse `Target <((HAS_CLASSIFICATION)) Host` are views of the same Relation fact.
HAS_CLASSIFICATION relates declared Entity or instance to applicable classification axis.
