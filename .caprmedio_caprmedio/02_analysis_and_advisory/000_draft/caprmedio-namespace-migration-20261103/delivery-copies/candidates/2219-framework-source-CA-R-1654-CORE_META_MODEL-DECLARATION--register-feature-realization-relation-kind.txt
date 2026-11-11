---
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//feature_realization
  passive:
  - CAPRMEDIO <+ MODEL <+ CFEL > Relation
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

