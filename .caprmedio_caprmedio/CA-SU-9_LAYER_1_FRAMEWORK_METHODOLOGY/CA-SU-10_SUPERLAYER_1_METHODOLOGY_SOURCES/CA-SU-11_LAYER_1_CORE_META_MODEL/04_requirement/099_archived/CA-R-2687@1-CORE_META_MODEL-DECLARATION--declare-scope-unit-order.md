---
atom_id: CA-R-2687
ref_id: CA-R-2687@1
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit.order
  dependencies:
  - CAPRMEDIO_MODEL <+ Scope Unit
tier: 3
status: archived
version: 1
updated_at: 2026-11-02 19:17:40 +0400
container:
  scope_unit: CA-SU-11
destination:
  file:
    name: CA-R-2687@1-CORE_META_MODEL-DECLARATION--declare-scope-unit-order.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
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
