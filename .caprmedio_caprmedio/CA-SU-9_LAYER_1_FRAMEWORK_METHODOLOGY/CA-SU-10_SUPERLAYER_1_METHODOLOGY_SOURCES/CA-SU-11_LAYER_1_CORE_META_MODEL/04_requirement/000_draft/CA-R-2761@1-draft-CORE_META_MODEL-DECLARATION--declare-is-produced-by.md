---
atom_id: CA-R-2761
ref_id: CA-R-2761@1-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_PRODUCED_BY
tier: 1
status: Draft
version: 1
updated_at: 2026-11-04 16:07:35 +0400
carrier_destination:
  file:
    name: CA-R-2761@1-draft-DECLARATION--declare-is-produced-by.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft
---

## Summary

Declare IS_PRODUCED_BY

## Claim

### Formal Claim

```CFEL
# model
Relation//IS_PRODUCED_BY <((HAS_INVERSE)) Relation//PRODUCES;

Relation//IS_PRODUCED_BY ((HAS_CLASSIFICATION)) Derivation == Derived;

# instances
Event//$event((IS_PRODUCED_BY)) Execution//$execution
```

## Semantics

IS_PRODUCED_BY links an Event to an Execution that produced it.
