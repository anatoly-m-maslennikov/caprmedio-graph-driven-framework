---
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//delivery_for
  passive:
  - CAPRMEDIO_MODEL <+ CFEL > Relation
version: 30
updated_at: 2026-11-03 20:00:05 +0400
relations: {}
atom_id: CA-R-1019
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-1019-CORE_META_MODEL-DECLARATION--register-delivery-for-relation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Register delivery_for relation

## Claim

### Formal Claim

```CFEL
# model
Relation//delivery_for ((HAS_CLASSIFICATION)) Derivation == Direct;

# instances
Atom/(.Header.Role: Delivery)//$atom ((delivery_for)) Atom//$atom_2
```

### Prose Claim

#### Applicability
`delivery_for` relations.

`delivery_for` **means** the direct relation from a Delivery Atom to the Atom
that the Delivery realizes.

Forward `Host ((delivery_for)) Target` and reverse `Target <((delivery_for)) Host` are views of the same Relation fact.
delivery_for relates Delivery Atom to realized Atom.
