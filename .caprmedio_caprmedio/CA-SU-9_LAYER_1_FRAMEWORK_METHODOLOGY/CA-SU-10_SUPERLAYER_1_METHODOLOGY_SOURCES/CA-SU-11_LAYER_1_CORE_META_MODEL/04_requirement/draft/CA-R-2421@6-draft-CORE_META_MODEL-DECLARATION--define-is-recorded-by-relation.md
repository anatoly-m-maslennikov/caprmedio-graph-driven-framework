---
atom_id: CA-R-2421
ref_id: CA-R-2421@6-draft
status: Draft
tier: 1
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_RECORDED_BY
version: 6
updated_at: 2026-11-04 16:07:35 +0400
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2421@6-draft-DECLARATION--define-is-recorded-by-relation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
container:
  scope_unit: CA-SU-11
---
## Summary

Define IS_RECORDED_BY Relation

## Claim

### Formal Claim

```CFEL
# model
Relation//IS_RECORDED_BY <((HAS_INVERSE)) Relation//RECORDS;

Relation//IS_RECORDED_BY ((HAS_CLASSIFICATION)) Derivation == Derived;

# instances
Event//$event((IS_RECORDED_BY)) Event Record//$record
```

## Semantics

IS_RECORDED_BY is the derived view from an Event to an Event Record of the stored RECORDS fact.
