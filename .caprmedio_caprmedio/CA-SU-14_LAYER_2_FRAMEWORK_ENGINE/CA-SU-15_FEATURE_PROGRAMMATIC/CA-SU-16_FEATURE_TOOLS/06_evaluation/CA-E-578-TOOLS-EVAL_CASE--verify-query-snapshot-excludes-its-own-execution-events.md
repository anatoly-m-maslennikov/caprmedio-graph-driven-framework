---
atom_id: CA-E-578
ref_id: CA-E-578
container:
  scope_unit: CA-SU-16
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record
  dependencies:
  - "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Source Retrieval"
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Action Run
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
tier: 4
relations:
  evaluation_for:
  - CA-R-1866
status: Active
version: 12
updated_at: 2026-10-27 19:59:37 +0400
carrier_destination:
  file:
    name: CA-E-578-TOOLS-EVAL_CASE--verify-query-snapshot-excludes-its-own-execution-events.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/06_evaluation
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
author: Anatoly Maslennikov
---
# Summary

Verify query snapshot excludes its own execution Events

## Claim

The Tool's result frontier remains unchanged when shared Run evidence appends during its actual invocation.

## Test case

Capture the Journal byte-prefix before workflow/action-start recording, start an
admitted execute invocation that records actual Run evidence, and append an
unrelated later Event before result pagination.

## Acceptance criteria

Returned IDs and continuation remain exactly the pre-dispatch snapshot; own and
later Events are absent, the result exposes the initial token and prefix hash,
and a standalone Action performs the same capture before its Run evidence.

## Failure disposition

Reject self-inclusion, frontier growth, or an unreported source change.
