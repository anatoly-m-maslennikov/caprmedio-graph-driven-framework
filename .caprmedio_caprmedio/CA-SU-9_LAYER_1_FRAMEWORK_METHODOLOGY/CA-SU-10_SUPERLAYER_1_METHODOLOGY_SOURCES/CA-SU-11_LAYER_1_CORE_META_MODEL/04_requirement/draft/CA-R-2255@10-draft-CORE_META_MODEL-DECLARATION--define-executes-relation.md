---
atom_id: CA-R-2255
status: Draft
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//EXECUTES
  passive:
  - CAPRMEDIO_MODEL <+ Runtime
  - CAPRMEDIO_MODEL <+ Execution
version: 10
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
tier: 1
updated_at: 2026-11-05 03:46:06 +0400
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2255@10-draft-CORE_META_MODEL-DECLARATION--define-executes-relation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
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
