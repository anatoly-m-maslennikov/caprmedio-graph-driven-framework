---
subjects:
  active: CFEL <+ Relation//structural_parent
  passive:
  - Scope Unit
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Structure
version: 35
updated_at: 2026-11-02 07:49:21 +0400
relations: {}
atom_id: CA-R-1660
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Declaration
---
## Summary

Register structural parent relation

## Claim scope

the Structural Parent Relation directed from a child to its immediate parent.

## Claim

the Structural Parent Relation **must** be the kind-independent Structural ownership relation directed from a child **to** its immediate parent. Project Structure owns Scope Unit parent declarations; structural graph views derive the corresponding `structural_parent` edge **without** maintaining a second source. a Carrier's physical containment **must not** silently replace a declared logical parent.

```CFEL
((structural_parent)) >| Derivation == Direct

$child ((structural_parent)) $parent
```

## Semantics



The Host is a structural child and the Target is its immediate structural parent.
Forward `Host ((structural_parent)) Target` and reverse `Target <((structural_parent)) Host` are views of the same Relation fact.
structural_parent relates structural child to immediate structural parent.

