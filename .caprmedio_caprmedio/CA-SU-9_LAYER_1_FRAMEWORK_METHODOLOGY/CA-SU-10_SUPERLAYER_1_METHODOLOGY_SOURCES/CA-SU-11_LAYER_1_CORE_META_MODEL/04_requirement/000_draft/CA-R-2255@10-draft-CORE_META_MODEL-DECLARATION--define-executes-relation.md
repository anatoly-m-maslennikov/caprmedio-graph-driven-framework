---
atom_id: CA-R-2255
ref_id: CA-R-2255@10-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//EXECUTES
  dependencies:
  - CAPRMEDIO_MODEL <+ Runtime
  - CAPRMEDIO_MODEL <+ Execution
tier: 1
status: Draft
version: 10
updated_at: 2026-11-05 03:46:06 +0400
carrier_destination:
  file:
    name: CA-R-2255@10-draft-DECLARATION--define-executes-relation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft
---
## Summary

Define EXECUTES Relation

## Claim

### Formal Claim

```CFEL
# model
Relation//EXECUTES ((HAS_INVERSE)) Relation//IS_EXECUTED_BY;

Relation//EXECUTES ((HAS_CLASSIFICATION)) Derivation == Direct;

# instances
Runtime//$runtime((EXECUTES)) Execution//$execution
```

## Semantics

EXECUTES is the stored Relation from a Runtime to an Execution. Its declared inverse IS_EXECUTED_BY is a derived view.
