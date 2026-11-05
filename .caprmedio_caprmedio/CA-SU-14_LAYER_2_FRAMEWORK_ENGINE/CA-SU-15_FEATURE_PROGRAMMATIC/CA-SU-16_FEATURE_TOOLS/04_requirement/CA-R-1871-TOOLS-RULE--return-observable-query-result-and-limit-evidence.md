---
atom_id: CA-R-1871
ref_id: CA-R-1871
container:
  scope_unit: CA-SU-16
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
tier: 3
status: Active
version: 8
updated_at: 2026-10-27 20:00:05 +0400
carrier_destination:
  file:
    name: CA-R-1871-TOOLS-RULE--return-observable-query-result-and-limit-evidence.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/04_requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
author: Anatoly Maslennikov
---
# Summary

Return observable query result and limit evidence

## Scope

The query result envelope.

## Claim

FIND_AND_FETCH_JOURNAL_EVENTS **must** return the snapshot token, result selection, pagination state, coverage state, and recoverable diagnostics sufficient to distinguish complete, partial, invalid, and blocked outcomes.

## Details

The envelope reports evidence and limits without exposing credentials, secrets, or unselected Event content.
