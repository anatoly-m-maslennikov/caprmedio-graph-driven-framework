---
atom_id: CA-R-1660
ref_id: CA-R-1660
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//structural_parent
  dependencies:
  - CAPRMEDIO_MODEL <+ Scope Unit
tier: 1
status: Active
version: 37
updated_at: 2026-11-03 20:00:05 +0400
carrier_destination:
  file:
    name: CA-R-1660-CORE_META_MODEL-DECLARATION--register-structural-parent-relation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Register structural parent relation

## Claim

### Prose Claim

#### Applicability
the Structural Parent Relation directed from a child to its immediate parent.

the Structural Parent Relation **must** be the kind-independent Structural ownership relation directed from a child **to** its immediate parent. Project Structure owns Scope Unit parent declarations; structural graph views derive the corresponding `structural_parent` edge **without** maintaining a second source. a Carrier's physical containment **must not** silently replace a declared logical parent.

The Host is a structural child and the Target is its immediate structural parent.
Forward `Host ((structural_parent)) Target` and reverse `Target <((structural_parent)) Host` are views of the same Relation fact.
structural_parent relates structural child to immediate structural parent.
### Formal Claim

```CFEL
# model
Relation//structural_parent ((HAS_CLASSIFICATION)) Derivation == Direct;

# instances
$child ((structural_parent)) $parent
```

