---
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//rationale_for
  passive:
  - CAPRMEDIO <+ MODEL <+ CFEL > Relation
version: 31
updated_at: 2026-11-02 15:49:28 +0400
relations: {}
atom_id: CA-R-1016
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1016-CORE_META_MODEL-DECLARATION--register-rationale-for-relation.md
  source_atom_id: CA-R-1016
  source_atom_revision: 31
  source_sha256: 15d42e205c1d59176a4d76f538e4716ba0c06a8216b2c683b7b951d40498e418
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Register rationale_for relation

## Claim scope

Rationale For Relation.

## Claim

`rationale_for` **means** the direct relation from a Rationale Analysis & Advisory Atom
to the Atom that it explains.

```CFEL
((rationale_for)) >| Derivation == Direct;

Atom/(.Role: "Analysis & Advisory")/(.Form: Rationale)// ((rationale_for)) Atom//
```

## Semantics


Forward `Host ((rationale_for)) Target` and reverse `Target <((rationale_for)) Host` are views of the same Relation fact.
rationale_for relates Rationale Analysis & Advisory Atom to explained Atom.

