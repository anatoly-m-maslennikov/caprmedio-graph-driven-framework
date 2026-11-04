---
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//feature_realization
  passive:
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
version: 38
updated_at: 2026-11-03 20:00:05 +0400
relations:
  child_of:
  - CA-R-1718
atom_id: CA-R-1654
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-1654-CORE_META_MODEL-DECLARATION--register-feature-realization-relation-kind.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1654-CORE_META_MODEL-DECLARATION--register-feature-realization-relation-kind.md
  source_atom_id: CA-R-1654
  source_atom_revision: 38
  source_sha256: f2117d0bf61ea4c0c2146cf65b3f689195bda3cddd008c6eed0cc6fa52838020
  original_relations_sha256: e505aa9ff1d066a0f7732fbe0bcf2c3da1556ffff64b77a4c92730c9625e58ef
---
## Summary

Register feature realization relation kind

## Claim

### Formal Claim

```CFEL
# model
Relation//feature_realization ((HAS_CLASSIFICATION)) Derivation == Direct;

# instances
Scope Unit//$scope_unit ((feature_realization)) $realization_target
```

### Prose Claim

#### Applicability
a declared SPEC Feature Scope Unit and its applicable native Realization targets.

`feature_realization` **must** be registered as a typed relation that maps a declared SPEC Feature Scope Unit **to** its applicable native Realization targets **without** making those targets Scope Units.

The Host is a SPEC Feature Scope Unit and the Target is its applicable native Realization.
Forward `Host ((feature_realization)) Target` and reverse `Target <((feature_realization)) Host` are views of the same Relation fact.
feature_realization relates SPEC Feature Scope Unit to applicable native Realization target.
