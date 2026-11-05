---
atom_id: CA-R-1862
ref_id: CA-R-1862
container:
  scope_unit: CA-SU-16
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record
tier: 3
status: Active
version: 11
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-R-1862-TOOLS-RULE--map-canonical-event-fields-to-the-shared-query-filter.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/04_requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
author: Anatoly Maslennikov
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
