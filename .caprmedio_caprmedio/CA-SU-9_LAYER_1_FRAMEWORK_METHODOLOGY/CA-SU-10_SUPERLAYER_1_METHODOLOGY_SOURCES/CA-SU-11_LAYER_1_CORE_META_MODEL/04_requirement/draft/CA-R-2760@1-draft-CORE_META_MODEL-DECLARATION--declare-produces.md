---
atom_id: CA-R-2760
status: Draft
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//PRODUCES
version: 1
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
tier: 1
role: Requirement
form: Declaration
updated_at: 2026-11-04 16:07:35 +0400
carrier_destination:
  file:
    name: CA-R-2760@1-draft-CORE_META_MODEL-DECLARATION--declare-produces.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
---

## Summary

Declare PRODUCES

## Claim

### Formal Claim

```CFEL
# model
Relation//PRODUCES ((HAS_INVERSE)) Relation//IS_PRODUCED_BY;

Relation//PRODUCES ((HAS_CLASSIFICATION)) Derivation == Direct;

# instances
Execution//$execution((PRODUCES)) Event//$event
```

## Semantics

PRODUCES links an Execution to an Event it produced.
