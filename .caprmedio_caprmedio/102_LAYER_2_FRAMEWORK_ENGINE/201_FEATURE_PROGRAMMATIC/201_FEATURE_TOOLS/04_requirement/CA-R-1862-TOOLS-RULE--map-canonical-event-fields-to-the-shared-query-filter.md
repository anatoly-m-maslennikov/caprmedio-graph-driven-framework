---
atom_id: CA-R-1862
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Active
author: Anatoly Maslennikov
version: 9
updated_at: 2026-10-27 06:04:45 +0400
subjects:
  governs: Subject/Graph Node/Domain/Continuant/History/Journal.Record
  depends_on: []
relations: {}
type: Rule
tier: 3
---
# Summary

Map canonical Event fields to the shared query filter

## Scope

The Journal-specific selector namespace for QUERY_FILTER.

## Claim

FIND_AND_FETCH_JOURNAL_EVENTS **must** expose every canonical Event field as a valid selector to CA-R-1850's shared QUERY_FILTER contract.

## Details

The namespace is `event:/<RFC6901-pointer>`: `event:/` addresses the complete
Event only for full-Event query, and every other selector is an RFC6901 pointer
from the Event root, including escaped object keys and array indices. A selector
is a JSON string under CA-R-1850's RFC8259 literal grammar. This mapping exposes
scalar, null, array, and object values without dot traversal or coercion; all
comparison semantics remain exactly CA-R-1850.
