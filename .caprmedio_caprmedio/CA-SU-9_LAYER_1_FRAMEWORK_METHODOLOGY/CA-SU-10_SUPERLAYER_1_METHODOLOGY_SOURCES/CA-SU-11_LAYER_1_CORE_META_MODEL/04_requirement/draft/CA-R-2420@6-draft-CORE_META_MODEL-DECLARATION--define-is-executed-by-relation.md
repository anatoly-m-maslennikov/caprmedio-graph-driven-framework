---
atom_id: CA-R-2420
ref_id: CA-R-2420@6-draft
status: Draft
tier: 1
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_EXECUTED_BY
version: 6
updated_at: 2026-11-04 16:07:35 +0400
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2420@6-draft-DECLARATION--define-is-executed-by-relation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
container:
  scope_unit: CA-SU-11
---
## Summary

Define IS_EXECUTED_BY Relation

## Claim

### Formal Claim

```CFEL
# model
Relation//IS_EXECUTED_BY <((HAS_INVERSE)) Relation//EXECUTES;

Relation//IS_EXECUTED_BY ((HAS_CLASSIFICATION)) Derivation == Derived;

# instances
Execution//$execution((IS_EXECUTED_BY)) Runtime//$runtime
```

## Semantics

IS_EXECUTED_BY is the derived view from an Execution to a Runtime of the stored EXECUTES fact.
