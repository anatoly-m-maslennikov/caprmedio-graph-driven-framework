---
atom_id: CA-M-335
ref_id: CA-M-335
container:
  scope_unit: CA-SU-16
role: Method
form: Eng Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record
tier: 4
relations:
  method_for:
  - CA-R-1850
  - CA-R-1862
  - CA-R-1868
  - CA-R-1869
status: Active
version: 11
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-M-335-TOOLS-ENG_DECISION--evaluate-shared-query-filters-against-event-selectors.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/05_method
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
author: Anatoly Maslennikov
---
# Summary

Evaluate shared query filters against Event selectors

## Scope

Journal selector binding to QUERY_FILTER.

## Claim

To evaluate an Event filter, the Tool **must** resolve Event selectors then apply CA-R-1850's shared QUERY_FILTER without altering its grammar or value semantics.

## Details

An unknown or ambiguous Event selector, or any shared-filter rejection, returns
the exact invalid-filter diagnostic and no partial match result.
