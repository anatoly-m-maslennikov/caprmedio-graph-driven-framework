---
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//method_for
  passive:
  - CAPRMEDIO <+ MODEL <+ CFEL > Relation
version: 30
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
atom_id: CA-R-1017
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1017-CORE_META_MODEL-DECLARATION--register-method-for-relation.md
  source_atom_id: CA-R-1017
  source_atom_revision: 30
  source_sha256: dce1fa546926b164b8bb2cf83ef0a83c407c49ceee0a9815518d3ea65f3a8aa6
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Register method_for relation

## Claim scope

Method For Relation.

## Claim

`method_for` **means** the direct relation from a Method Atom to the
Requirement Atom that the Method serves.

```CFEL
((method_for)) >| Derivation == Direct;

Atom/(.Role: Method)// ((method_for)) Atom/(.Role: Requirement)//
```

## Semantics


Forward `Host ((method_for)) Target` and reverse `Target <((method_for)) Host` are views of the same Relation fact.
method_for relates Method Atom to served Requirement Atom.

