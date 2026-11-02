---
atom_id: CA-R-1868@5
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 5
updated_at: 2026-10-24 11:58:20 +0400
subjects:
  governs: Subject/Domain/Node/Continuant/History/Journal.Record
  depends_on:
  - Subject/Engineering/Journal Event Query/Selector Value Semantics
relations:
  relates_to:
  - CA-R-1850
  - CA-R-1862
  - CA-E-575
type: Rule
tier: 3
---
# Summary

Map Event field values without changing shared filter semantics

## Scope

The Journal-specific selector value extraction.

## Claim

FIND_AND_FETCH_JOURNAL_EVENTS **must** pass each selected canonical Event field's exact value state to CA-R-1850 without coercion, normalization, or inferred filename value.

## Details

The Tool marks absent selectors as absent and explicit null as null. Arrays and
objects are passed as parsed RFC8259 structural values, including nested fields
resolved by RFC6901 pointers, without stringification or flattening. It delegates
all comparison and invalid-literal decisions to CA-R-1850.
