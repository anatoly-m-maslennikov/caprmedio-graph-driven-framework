---
atom_id: CA-R-2557
ref_id: CA-R-2557@5-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Event Record
tier: 3
status: Draft
version: 5
updated_at: 2026-11-05 13:47:13 +0400
carrier_destination:
  file:
    name: CA-R-2557@5-draft-DECLARATION--declare-event-record.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
---
## Summary

Declare Event Record

## Claim

### Prose Claim


An Event Record is immutable.


### Formal Claim

```CFEL
# model
Event Record {::0}((IS_PROPERTY_OF));

Event Record ((NARROWER_THAN)) Continuant;

# instances
Event Record//$event_record {::1}((IS_CONTAINED_BY)) Journal//$journal;

$event_record {::1}((RECORDS)) Event//$event
```

## Semantics

An Event Record is a persistent description of an event and its recorded evidence.
