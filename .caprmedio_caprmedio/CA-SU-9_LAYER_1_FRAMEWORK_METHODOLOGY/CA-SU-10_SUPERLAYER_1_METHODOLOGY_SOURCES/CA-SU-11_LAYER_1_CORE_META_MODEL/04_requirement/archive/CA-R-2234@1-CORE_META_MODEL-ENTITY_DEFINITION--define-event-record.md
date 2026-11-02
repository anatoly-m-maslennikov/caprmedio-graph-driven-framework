---
atom_id: CA-R-2234@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Object/Continuant/History/Journal > Event Record
  depends_on:
  - Entity/Object/Continuant/History/Journal
  - Entity/Object/Occurrent/Execution/Workflow Run
  - Entity/Graph Syntax > Relation//RECORDS
  - Entity/Object/Occurrent/Execution.Result
version: 1
updated_at: 2026-10-29 07:32:39 +0400
relations: {}
tier: 1
---
## Summary

Define Event Record

## Claim

An Event Record is a persistent record within exactly one Journal that describes something that happened. It can RECORD an actual occurrence, including a Workflow Run. The record is not the occurrence itself. It can preserve or describe an actual Execution.Result.

### Formal claim

```text
Journal > Event Record
Event Record ((RECORDS)) Workflow Run
```

## Semantics

The Workflow Run edge is the requested model case, not a declaration that all records must describe Workflow Runs. The Journal contains the record; it does not contain the actual occurrence. A record's Carrier represents that record, not the living execution. IS_RECORDED_BY is the derived opposite view of RECORDS, not another stored fact.

## Details


CA-A-1276 distinguishes the recorded result from the execution and from its API contract; it adds no mandatory result field or recording obligation.
