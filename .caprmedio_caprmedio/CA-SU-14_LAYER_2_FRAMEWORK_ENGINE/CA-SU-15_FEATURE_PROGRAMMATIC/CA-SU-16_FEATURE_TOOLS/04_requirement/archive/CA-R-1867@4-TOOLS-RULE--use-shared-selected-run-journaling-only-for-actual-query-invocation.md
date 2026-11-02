---
atom_id: CA-R-1867@4
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 4
updated_at: 2026-10-24 11:58:20 +0400
subjects:
  governs: Subject/Domain/Node/Occurrent/Execution
  depends_on:
  - Subject/Domain/Node/Occurrent/Execution
  - Subject/Domain/Node/Continuant/History/Journal
  - Subject/Domain/Node/Continuant/History/Journal.Record
  - Subject/Engineering/Journal Event Query/Actual Invocation Recording
relations:
  relates_to:
  - CA-O-161
  - CA-D-527
  - CA-D-528
  - CA-D-529
  - CA-E-580
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
