---
atom_id: CA-R-2767
ref_id: CA-R-2767
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_SPECIALIZED_BY
tier: 1
status: Active
version: 2
updated_at: 2026-11-04 19:46:41 +0400
carrier_destination:
  file:
    name: CA-R-2767-DECLARATION--declare-is-specialized-by.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2767-CORE_META_MODEL-DECLARATION--declare-is-specialized-by.md
  source_atom_id: CA-R-2767
  source_atom_revision: 2
  source_sha256: a632f266c24fe5d3f15c71d1cd5c81d2b7305aa429eb4e6464e47d69ddf467cc
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare IS_SPECIALIZED_BY

## Claim

### Formal Claim

```CFEL
# model
Relation//IS_SPECIALIZED_BY <((HAS_INVERSE)) Relation//SPECIALIZES;

Relation//IS_SPECIALIZED_BY ((HAS_CLASSIFICATION)) Derivation == Derived;

# instances
Atom//$parent ((IS_SPECIALIZED_BY)) Atom//$child
```

## Semantics

IS_SPECIALIZED_BY relates an Atom to an Atom whose Claim specializes its Claim.
