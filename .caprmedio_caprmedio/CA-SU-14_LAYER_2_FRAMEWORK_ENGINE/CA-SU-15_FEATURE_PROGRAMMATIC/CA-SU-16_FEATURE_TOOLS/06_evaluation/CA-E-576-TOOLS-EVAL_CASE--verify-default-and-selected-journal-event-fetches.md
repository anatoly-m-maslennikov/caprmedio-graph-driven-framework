---
atom_id: CA-E-576
ref_id: CA-E-576
container:
  scope_unit: CA-SU-16
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record
  dependencies:
  - "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Source Retrieval"
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
tier: 4
relations:
  evaluation_for:
  - CA-R-1863
status: Active
version: 10
updated_at: 2026-10-27 19:59:37 +0400
carrier_destination:
  file:
    name: CA-E-576-TOOLS-EVAL_CASE--verify-default-and-selected-journal-event-fetches.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/06_evaluation
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
author: Anatoly Maslennikov
---
# Summary

Verify default and selected Journal Event fetches

## Claim

The Tool returns only Event IDs by default and returns only explicitly selected fields or full Events when requested.

## Test case

Query one snapshot in default, selected-field, full-Event, and missing-selected-field modes.

## Acceptance criteria

Default records contain only canonical IDs; selected mode preserves requested field order; full mode preserves Event content; missing values remain explicit diagnostics.

## Failure disposition

Reject unrequested Event content, filename IDs, or synthesized missing values.
