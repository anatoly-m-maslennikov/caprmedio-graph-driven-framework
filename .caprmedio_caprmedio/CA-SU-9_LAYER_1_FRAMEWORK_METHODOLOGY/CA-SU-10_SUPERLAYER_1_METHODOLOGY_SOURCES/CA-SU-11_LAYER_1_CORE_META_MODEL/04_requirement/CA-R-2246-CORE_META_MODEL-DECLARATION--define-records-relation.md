---
atom_id: CA-R-2246
ref_id: CA-R-2246
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//RECORDS
  dependencies:
  - CAPRMEDIO_MODEL <+ Event Record
  - CAPRMEDIO_MODEL <+ Entity/Object/Occurrent/Execution/Workflow Run
version: 8
tier: 1
updated_at: 2026-11-03 20:00:05 +0400
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2246-CORE_META_MODEL-DECLARATION--define-records-relation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
container:
  scope_unit: CA-SU-11
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
Event Record//$event_record ((RECORDS)) $occurrence
```

### Prose Claim

RECORDS connects an Event Record to the actual occurrence described by that
record. The stored direction is Event Record to the actual Event or execution it records. IS_RECORDED_BY
is its declared derived inverse, not a second stored fact.

The Target is the actual Event or execution described by the Event Record.
Forward `Host ((RECORDS)) Target` and reverse `Target <((RECORDS)) Host` are views of the same Relation fact.
Event Record ((RECORDS)) Workflow Run

A Workflow Run is one recorded occurrence kind, not the only one. The Event
Record persists independently of that Occurrent. This Definition imposes no
record-count constraint.

#### Details
This named Type uses the general `((RELATION_TYPE))` form. It defines the reusable Type and creates no occurrence or actual endpoint tuple.
