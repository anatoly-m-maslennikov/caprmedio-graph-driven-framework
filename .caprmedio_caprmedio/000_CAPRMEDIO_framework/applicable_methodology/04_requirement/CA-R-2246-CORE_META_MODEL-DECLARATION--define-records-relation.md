---
atom_id: CA-R-2246
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CFEL <+ Relation//RECORDS
  passive:
  - Entity/Object/Continuant/History/Journal > Event Record
  - Entity/Object/Occurrent/Execution/Workflow Run
version: 7
relations: {}
tier: 1
updated_at: 2026-11-02 08:06:47 +0400
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2246-CORE_META_MODEL-DECLARATION--define-records-relation.md
  source_atom_id: CA-R-2246
  source_atom_revision: 7
  source_sha256: 3c2c9ba081047a61152fffcb803b98f766098f8ba490e66c99735928649b51f6
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define RECORDS Relation

## Claim

RECORDS connects an Event Record to the actual occurrence described by that
record. The stored direction is Event Record to the actual Event or execution it records. IS_RECORDED_BY
is its declared derived inverse, not a second stored fact.

```CFEL
((RECORDS)) ((HAS_INVERSE)) ((IS_RECORDED_BY));

((RECORDS)) >| Derivation == Direct;

Event Record// ((RECORDS)) $occurrence
```

## Semantics



The Target is the actual Event or execution described by the Event Record.
Forward `Host ((RECORDS)) Target` and reverse `Target <((RECORDS)) Host` are views of the same Relation fact.
Event Record ((RECORDS)) Workflow Run

A Workflow Run is one recorded occurrence kind, not the only one. The Event
Record persists independently of that Occurrent. This Definition imposes no
record-count constraint.

## Details

This named Type uses the general `((RELATION_TYPE))` form. It defines the reusable Type and creates no occurrence or actual endpoint tuple.
