---
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//concern_about
  passive:
  - CAPRMEDIO <+ MODEL <+ CFEL > Relation
version: 31
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
atom_id: CA-R-1022
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1022-CORE_META_MODEL-DECLARATION--register-concern-about-relation.md
  source_atom_id: CA-R-1022
  source_atom_revision: 31
  source_sha256: 3884e4a7d4c75cb343eb60f1857b66b73abd57c2df39bcc26758dd29f0c3ee81
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Register concern_about relation

## Claim scope

`concern_about` relations.

## Claim

`concern_about` **means** the direct relation from a Concern Atom to the
governed entity that it concerns.

```CFEL
((concern_about)) >| Derivation == Direct;

Atom/(.Role: Concern)// ((concern_about)) $governed
```

## Semantics



The Host is a Concern Atom; the governed target is the Entity concerned.
Forward `Host ((concern_about)) Target` and reverse `Target <((concern_about)) Host` are views of the same Relation fact.
concern_about relates Concern Atom to governed entity concerned.

## Details

Endpoint admission is an Atom Entity Definition concern, not Relation Definition
metadata.
