---
atom_id: CA-R-1867
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Active
author: Anatoly Maslennikov
version: 8
updated_at: 2026-10-27 20:00:04 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Execution
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record
relations: {}
type: Rule
tier: 3
---
# Summary

Use shared selected-Run journaling only for actual query invocation

## Scope

Query Run evidence.

## Claim

FIND_AND_FETCH_JOURNAL_EVENTS **must** use the shared RunJournal contract for actual invocation and must not create a competing log, fake Run, or preview Event.

## Details

CA-D-527, CA-D-528, and CA-D-529 govern preview/execute distinction, durable evidence, and delivery placement; this route contributes no second executor or Journal format.
