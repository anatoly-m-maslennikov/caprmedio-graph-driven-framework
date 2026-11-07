---
atom_id: CA-R-2601
ref_id: CA-R-2601
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL<+Operator//Grouping
tier: 3
status: Active
version: 3
updated_at: 2026-11-04 21:11:03 +0400
carrier_destination:
  file:
    name: CA-R-2601-DECLARATION--declare-cfel-operator.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2601-CORE_META_MODEL-DECLARATION--declare-cfel-operator.md
  source_atom_id: CA-R-2601
  source_atom_revision: 3
  source_sha256: 304cb09b1e5f8732bc919cab8899371a50a4c575e0f66042f0b5303e29e8d207
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare CFEL operator ()

## Claim

### Formal Claim

```CFEL
# model
Operator//Grouping == "()"
```

## Semantics

Group one CFEL expression; parentheses do not create a Node or Relation. When AND and OR occur in one Boolean expression, use parentheses to make their grouping explicit; neither has implicit precedence over the other.
