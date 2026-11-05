---
atom_id: CA-M-336
ref_id: CA-M-336
container:
  scope_unit: CA-SU-16
role: Method
form: Eng Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record
tier: 4
relations:
  method_for:
  - CA-R-1863
  - CA-R-1865
  - CA-R-1871
status: Active
version: 11
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-M-336-TOOLS-ENG_DECISION--select-and-page-event-query-results.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/05_method
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
author: Anatoly Maslennikov
---
# Summary

Select and page Event query results

## Scope

Result construction.

## Claim

To construct results, the Tool **must** order snapshot matches deterministically, apply the bounded page, and expose IDs, selected fields, or full Events only in the requested mode with truthful coverage metadata.

## Details

The next-page token remains bound to the source snapshot, source/prefix hashes,
result selection, and configured limits. Before any continuation it revalidates
captured members and rejects changed, deleted, unreadable, or truncated captured
data, while allowing append strictly after the sealed prefix.
