---
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//evaluation_for
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Evaluation)
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Requirement)
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Method)
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Delivery)
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Operations)
  - CAPRMEDIO <+ MODEL <+ Atom.Tier
version: 37
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
atom_id: CA-R-1018
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1018-CORE_META_MODEL-DECLARATION--register-evaluation-targets.md
  source_atom_id: CA-R-1018
  source_atom_revision: 37
  source_sha256: e381a9d2a27c6ab86232c9dd100bbaaf88630f233fba73c11dfbc23afcbac5ca
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Register Evaluation targets

## Claim scope

direct `evaluation_for` relations.

## Claim

`evaluation_for` **means** the direct relation from an Evaluation Atom to an
Atom whose authority the Evaluation checks.

```CFEL
((evaluation_for)) >| Derivation == Direct;

Atom/(.Role: Evaluation)// ((evaluation_for)) Atom//
```

## Semantics


Forward `Host ((evaluation_for)) Target` and reverse `Target <((evaluation_for)) Host` are views of the same Relation fact.
evaluation_for relates Evaluation Atom to Atom whose authority is evaluated.

