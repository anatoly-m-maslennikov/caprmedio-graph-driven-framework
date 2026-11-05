---
atom_id: CA-R-2477
ref_id: CA-R-2477
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//HAS_CLASSIFICATION
version: 5
updated_at: 2026-11-03 20:00:05 +0400
tier: 3
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2477-CORE_META_MODEL-DECLARATION--define-classification-and-its-written-reverse.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
container:
  scope_unit: CA-SU-11
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
