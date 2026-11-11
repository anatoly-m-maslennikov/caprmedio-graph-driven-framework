---
atom_id: CA-R-2246
ref_id: CA-R-2246@9-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//RECORDS
  dependencies:
  - CAPRMEDIO_MODEL <+ Event Record
  - CAPRMEDIO_MODEL <+ Event
tier: 1
status: Draft
version: 9
updated_at: 2026-11-04 16:07:35 +0400
carrier_destination:
  file:
    name: CA-R-2246@9-draft-DECLARATION--define-records-relation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft
---
## Summary

Define RECORDS Relation

## Claim

### Formal Claim

```CFEL
# model
Relation//RECORDS ((HAS_INVERSE)) Relation//IS_RECORDED_BY;

Relation//RECORDS ((HAS_CLASSIFICATION)) Derivation == Direct;

# instances
Event Record//$event_record((RECORDS)) Event//$event
```

## Semantics

RECORDS is the stored Relation from an Event Record to the Event it describes. Its declared inverse IS_RECORDED_BY is a derived view; an Event Record is distinct from the Event.
