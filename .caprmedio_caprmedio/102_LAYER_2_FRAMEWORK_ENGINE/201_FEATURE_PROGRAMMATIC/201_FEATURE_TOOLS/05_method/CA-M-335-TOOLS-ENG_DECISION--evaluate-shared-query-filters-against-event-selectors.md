---
atom_id: CA-M-335
content_role: Method
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Active
author: Anatoly Maslennikov
version: 10
updated_at: 2026-10-27 19:59:42 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record
  depends_on: []
relations:
  method_for:
  - CA-R-1850
  - CA-R-1862
  - CA-R-1868
  - CA-R-1869
type: Eng Decision
tier: 4
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
