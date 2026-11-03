---
subjects:
  active: CFEL <+ Relation//structural_parent
  passive:
  - Scope Unit
version: 36
updated_at: 2026-11-02 19:44:26 +0400
relations: {}
atom_id: CA-R-1660
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1660-CORE_META_MODEL-DECLARATION--register-structural-parent-relation.md
  source_atom_id: CA-R-1660
  source_atom_revision: 36
  source_sha256: 9ee2853560543d6ec1dfb85eb989102d54269379738be0a4badd3e3c63f4d0b9
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Register structural parent relation

## Claim scope

the Structural Parent Relation directed from a child to its immediate parent.

## Claim

the Structural Parent Relation **must** be the kind-independent Structural ownership relation directed from a child **to** its immediate parent. Project Structure owns Scope Unit parent declarations; structural graph views derive the corresponding `structural_parent` edge **without** maintaining a second source. a Carrier's physical containment **must not** silently replace a declared logical parent.

```CFEL
((structural_parent)) >| Derivation == Direct;

$child ((structural_parent)) $parent
```

## Semantics



The Host is a structural child and the Target is its immediate structural parent.
Forward `Host ((structural_parent)) Target` and reverse `Target <((structural_parent)) Host` are views of the same Relation fact.
structural_parent relates structural child to immediate structural parent.

