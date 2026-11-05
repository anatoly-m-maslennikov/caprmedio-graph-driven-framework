---
atom_id: CA-R-1019
ref_id: CA-R-1019
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//delivery_for
  dependencies:
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
tier: 1
status: Active
version: 30
updated_at: 2026-11-03 20:00:05 +0400
carrier_destination:
  file:
    name: CA-R-1019-CORE_META_MODEL-DECLARATION--register-delivery-for-relation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1019-CORE_META_MODEL-DECLARATION--register-delivery-for-relation.md
  source_atom_id: CA-R-1019
  source_atom_revision: 30
  source_sha256: 980d828d2c3d6de10927926c10e6d651e771c361eb4c826546b0814fee84f20e
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Register delivery_for relation

## Claim

### Prose Claim

#### Applicability
`delivery_for` relations.

`delivery_for` **means** the direct relation from a Delivery Atom to the Atom
that the Delivery realizes.

Forward `Host ((delivery_for)) Target` and reverse `Target <((delivery_for)) Host` are views of the same Relation fact.
delivery_for relates Delivery Atom to realized Atom.
### Formal Claim

```CFEL
# model
Relation//delivery_for ((HAS_CLASSIFICATION)) Derivation == Direct;

# instances
Atom/(.Header.Role: Delivery)//$atom ((delivery_for)) Atom//$atom_2
```

