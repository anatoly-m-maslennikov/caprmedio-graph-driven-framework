---
atom_id: CA-R-2557
ref_id: CA-R-2557
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Event Record
tier: 3
status: Active
version: 4
updated_at: 2026-11-02 08:06:47 +0400
carrier_destination:
  file:
    name: CA-R-2557-CORE_META_MODEL-DECLARATION--declare-event-record.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2557-CORE_META_MODEL-DECLARATION--declare-event-record.md
  source_atom_id: CA-R-2557
  source_atom_revision: 4
  source_sha256: e145e57587e9d228a8e0b8b092f7ac4e17cc65e8e61ef77189539df822f654d8
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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
Event Record//$event_record {::1}((IS_CONTAINED_BY)) Journal//$journal
```

## Semantics

An Event Record is a persistent description of an event and its recorded evidence.
