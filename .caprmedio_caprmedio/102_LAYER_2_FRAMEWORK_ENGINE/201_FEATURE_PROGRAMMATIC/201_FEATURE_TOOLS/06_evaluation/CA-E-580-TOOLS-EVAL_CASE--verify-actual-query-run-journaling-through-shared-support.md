---
atom_id: CA-E-580
content_role: Evaluation
type: Eval Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Active
author: Anatoly Maslennikov
version: 12
updated_at: 2026-10-27 19:59:37 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Action Run
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Source Retrieval
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
relations:
  evaluation_for:
  - CA-R-1867
tier: 4
---
# Summary

Verify actual query Run journaling through shared support

## Claim

The Tool creates shared RunJournal evidence only for an actual admitted query execution and creates none for preview or denied requests.

## Test case

Run preview, denied execute, and admitted execute against a source whose
byte-prefix is captured before workflow/action-start recording.

## Acceptance criteria

Preview and denial have no Run/Event identity; admitted execute has truthful Workflow/Step/Action lineage and cannot affect its result snapshot.

## Failure disposition

Reject fake Runs, preview Events, competing logs, or snapshot mutation.
