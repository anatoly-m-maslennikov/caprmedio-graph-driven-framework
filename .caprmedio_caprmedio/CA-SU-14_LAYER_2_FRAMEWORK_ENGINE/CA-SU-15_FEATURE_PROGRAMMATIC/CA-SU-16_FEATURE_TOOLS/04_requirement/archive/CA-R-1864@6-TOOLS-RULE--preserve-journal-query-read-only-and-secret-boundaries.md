---
atom_id: CA-R-1864@6
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 6
updated_at: 2026-10-26 00:46:35 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Aspect/Data Handling/Source Retrieval
  depends_on:
  - Subject/Graph Node/Domain/Continuant/History/Journal
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
relations:
  relates_to:
  - CA-O-162
  - CA-E-579
type: Rule
tier: 3
---
# Summary

Preserve Journal query read-only and secret boundaries

## Scope

The query authorization boundary.

## Claim

FIND_AND_FETCH_JOURNAL_EVENTS **must not** create mutation authority, read credentials or secrets, or evaluate arbitrary SQL or code.

## Details

Rejected inputs and redacted protected values are reported as boundaries, not fetched, logged, or transformed into authority.
