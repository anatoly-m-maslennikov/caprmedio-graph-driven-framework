---
atom_id: CA-M-335@3
content_role: Method
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 3
updated_at: 2026-10-23 23:09:56 +0400
subjects:
  governs: Subject/Domain/Node/Continuant/History/Journal.Record
  depends_on:
  - Subject/Engineering/Journal Event Query/Selector Evaluation
  - Subject/Engineering/Query Filter Contract
relations:
  method_for:
  - CA-R-1850
  - CA-R-1862
  - CA-R-1868
  - CA-R-1869
type: Eng Decision
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
