---
atom_id: CA-E-580
ref_id: CA-E-580
container:
  scope_unit: CA-SU-16
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Action Run
  - "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Source Retrieval"
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
tier: 4
relations:
  evaluation_for:
  - CA-R-1867
status: Active
version: 12
updated_at: 2026-10-27 19:59:37 +0400
carrier_destination:
  file:
    name: CA-E-580-TOOLS-EVAL_CASE--verify-actual-query-run-journaling-through-shared-support.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/06_evaluation
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
author: Anatoly Maslennikov
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
