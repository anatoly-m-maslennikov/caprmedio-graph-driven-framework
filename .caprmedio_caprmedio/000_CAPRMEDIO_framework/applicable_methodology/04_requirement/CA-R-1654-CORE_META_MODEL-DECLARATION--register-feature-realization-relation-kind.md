---
subjects:
  active: CFEL <+ Relation//feature_realization
  passive:
  - CFEL > Relation
version: 37
updated_at: 2026-11-02 08:06:47 +0400
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
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1654-CORE_META_MODEL-DECLARATION--register-feature-realization-relation-kind.md
  source_atom_id: CA-R-1654
  source_atom_revision: 37
  source_sha256: 45785814b3b8a2784b1339a6319303a04779c05bb1c91afd7fdd40319d59c1bc
  original_relations_sha256: e505aa9ff1d066a0f7732fbe0bcf2c3da1556ffff64b77a4c92730c9625e58ef
---
## Summary

Register feature realization relation kind

## Claim scope

a declared SPEC Feature Scope Unit and its applicable native Realization targets.

## Claim

`feature_realization` **must** be registered as a typed relation that maps a declared SPEC Feature Scope Unit **to** its applicable native Realization targets **without** making those targets Scope Units.

```CFEL
((feature_realization)) >| Derivation == Direct;

Scope Unit// ((feature_realization)) $realization_target
```

## Semantics



The Host is a SPEC Feature Scope Unit and the Target is its applicable native Realization.
Forward `Host ((feature_realization)) Target` and reverse `Target <((feature_realization)) Host` are views of the same Relation fact.
feature_realization relates SPEC Feature Scope Unit to applicable native Realization target.

