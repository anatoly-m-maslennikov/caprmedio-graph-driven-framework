---
atom_id: CA-R-2557
ref_id: CA-R-2557
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
topics:
  main_subject: CAPRMEDIO_MODEL <+ Event Record
version: 4
updated_at: 2026-11-02 08:06:47 +0400
tier: 3
role: Requirement
form: Declaration
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-R-2557-CORE_META_MODEL-DECLARATION--declare-event-record.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare Event Record

## Claim

### Formal Claim

```CFEL
# model
Event Record {::0}((IS_PROPERTY_OF));

Event Record ((NARROWER_THAN)) Continuant;

# instances
Event Record//$event_record {::1}((IS_CONTAINED_BY)) Journal//$journal
```

### Prose Claim


An Event Record is immutable.


## Semantics

An Event Record is a persistent description of an event and its recorded evidence.
