---
atom_id: CA-R-2755
ref_id: CA-R-2755@1-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Event
tier: 3
status: Draft
version: 1
updated_at: 2026-11-05 01:38:59 +0400
carrier_destination:
  file:
    name: CA-R-2755@1-draft-DECLARATION--declare-event.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft
---

## Summary

Declare Event

## Claim

### Formal Claim

```CFEL
# model
Event ((NARROWER_THAN)) Occurrent;

# instances
Event//$event {::0+}((IS_RECORDED_BY)) Event Record//$record;

Event//$produced_event {::1+}((IS_PRODUCED_BY)) Execution//$producer
```

## Semantics

An Event is an occurrence produced by an Execution.
