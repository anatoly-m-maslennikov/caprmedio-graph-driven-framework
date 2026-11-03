---
atom_id: CA-R-2246
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//RECORDS
  passive:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/History/Journal > Event Record
  - CAPRMEDIO_MODEL <+ Entity/Object/Occurrent/Execution/Workflow Run
version: 7
relations: {}
tier: 1
updated_at: 2026-11-02 08:06:47 +0400
role: Requirement
form: Declaration
---
## Summary

Define RECORDS Relation

## Claim

### Formal Claim

```CFEL
Relation//RECORDS ((HAS_INVERSE)) Relation//IS_RECORDED_BY;

Relation//RECORDS ((HAS_CLASSIFICATION)) Derivation == Direct;

Event Record// ((RECORDS)) $occurrence
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
