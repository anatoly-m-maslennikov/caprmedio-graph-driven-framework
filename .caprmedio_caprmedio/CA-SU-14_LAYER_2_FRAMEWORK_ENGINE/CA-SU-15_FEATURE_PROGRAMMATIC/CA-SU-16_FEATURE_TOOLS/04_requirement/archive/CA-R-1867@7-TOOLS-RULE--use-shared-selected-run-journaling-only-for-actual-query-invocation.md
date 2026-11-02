---
atom_id: CA-R-1867@7
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 7
updated_at: 2026-10-27 06:04:45 +0400
subjects:
  governs: Subject/Graph Node/Domain/Occurrent/Execution
  depends_on:
  - Subject/Graph Node/Domain/Occurrent/Execution
  - Subject/Graph Node/Domain/Continuant/History/Journal
  - Subject/Graph Node/Domain/Continuant/History/Journal.Record
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
