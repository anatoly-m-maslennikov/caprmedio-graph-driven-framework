---
atom_id: CA-R-2687
ref_id: CA-R-2687
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit.order
  dependencies:
  - CAPRMEDIO_MODEL <+ Scope Unit
tier: 3
status: Active
version: 1
updated_at: 2026-11-02 19:17:40 +0400
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2687-CORE_META_MODEL-DECLARATION--declare-scope-unit-order.md
  source_atom_id: CA-R-2687
  source_atom_revision: 1
  source_sha256: 528dfc938400f564b6035d6c245df682b73a72e3f9b83ef977f1d82e339717f5
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Scope Unit.order

## Claim

### Formal Claim

```CFEL
# model
Scope Unit.order:: []{::0};

Scope Unit.order.*[in (ordered, number)]{::1..2}
```

## Semantics

order groups the Boolean ordered and the conditional number as sibling Properties. The group has no direct value.
