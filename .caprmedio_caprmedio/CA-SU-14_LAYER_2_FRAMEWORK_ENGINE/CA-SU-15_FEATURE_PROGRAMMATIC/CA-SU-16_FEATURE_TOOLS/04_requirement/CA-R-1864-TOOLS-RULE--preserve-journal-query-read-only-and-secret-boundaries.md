---
atom_id: CA-R-1864
ref_id: CA-R-1864
role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Active
author: Anatoly Maslennikov
version: 9
updated_at: 2026-10-27 20:00:04 +0400
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Source Retrieval
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
form: Rule
tier: 3
container:
  scope_unit: CA-SU-16
carrier_destination:
  file:
    name: CA-R-1864-TOOLS-RULE--preserve-journal-query-read-only-and-secret-boundaries.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/04_requirement
---
# Summary

Preserve Journal query read-only and secret boundaries

## Scope

The query authorization boundary.

## Claim

FIND_AND_FETCH_JOURNAL_EVENTS **must not** create mutation authority, read credentials or secrets, or evaluate arbitrary SQL or code.

## Details

Rejected inputs and redacted protected values are reported as boundaries, not fetched, logged, or transformed into authority.
