---
atom_id: CA-R-2246@1
content_role: Requirement
type: Relation Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Graph Syntax > Relation//RECORDS
  depends_on:
  - Entity/Object/Continuant/History/Journal > Event Record
  - Entity/Object/Occurrent/Execution/Workflow Run
version: 1
relations: {}
tier: 1
updated_at: 2026-10-29 07:32:39 +0400
---
## Summary

Define RECORDS Relation

## Claim

RECORDS connects an Event Record to the actual occurrence described by that
record. The stored direction is Event Record to the actual Event or execution it records. IS_RECORDED_BY
is its declared derived inverse, not a second stored fact.

### Formal claim

```yaml
relation_type: RECORDS
meaning: Connect an Event Record to the actual occurrence described by that record.
derived_inverse: IS_RECORDED_BY
stored_fact: direct_only
```

## Semantics

Event Record ((RECORDS)) Workflow Run

A Workflow Run is one recorded occurrence kind, not the only one. The Event
Record persists independently of that Occurrent. This Definition imposes no
record-count constraint.

## Details

This named Type uses the general `((RELATION_TYPE))` form. It has no dedicated
short Entity operator, so `content.notation_for_subject` is intentionally
absent. This Draft creates neither a Current registration nor a runtime fact.
