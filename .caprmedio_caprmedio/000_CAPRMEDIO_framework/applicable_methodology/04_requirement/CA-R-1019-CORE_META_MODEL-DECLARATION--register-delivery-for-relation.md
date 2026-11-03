---
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//delivery_for
  passive:
  - CAPRMEDIO <+ MODEL <+ CFEL > Relation
version: 29
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
atom_id: CA-R-1019
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1019-CORE_META_MODEL-DECLARATION--register-delivery-for-relation.md
  source_atom_id: CA-R-1019
  source_atom_revision: 29
  source_sha256: 75169dde1b2948b402bd6d691a2829f32dd9315b26cbf4660bec400ca8f59d87
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Register delivery_for relation

## Claim scope

`delivery_for` relations.

## Claim

`delivery_for` **means** the direct relation from a Delivery Atom to the Atom
that the Delivery realizes.

```CFEL
((delivery_for)) >| Derivation == Direct;

Atom/(.Role: Delivery)// ((delivery_for)) Atom//
```

## Semantics


Forward `Host ((delivery_for)) Target` and reverse `Target <((delivery_for)) Host` are views of the same Relation fact.
delivery_for relates Delivery Atom to realized Atom.

