---
atom_id: CA-R-1654
ref_id: CA-R-1654@38
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//feature_realization
  dependencies:
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
tier: 3
relations:
  child_of:
  - CA-R-1718
status: archived
version: 38
updated_at: 2026-11-03 20:00:05 +0400
carrier_destination:
  file:
    name: CA-R-1654@38-CORE_META_MODEL-DECLARATION--register-feature-realization-relation-kind.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Register feature realization relation kind

## Claim

### Prose Claim

#### Applicability
a declared SPEC Feature Scope Unit and its applicable native Realization targets.

`feature_realization` **must** be registered as a typed relation that maps a declared SPEC Feature Scope Unit **to** its applicable native Realization targets **without** making those targets Scope Units.

The Host is a SPEC Feature Scope Unit and the Target is its applicable native Realization.
Forward `Host ((feature_realization)) Target` and reverse `Target <((feature_realization)) Host` are views of the same Relation fact.
feature_realization relates SPEC Feature Scope Unit to applicable native Realization target.
### Formal Claim

```CFEL
# model
Relation//feature_realization ((HAS_CLASSIFICATION)) Derivation == Direct;

# instances
Scope Unit//$scope_unit ((feature_realization)) $realization_target
```

