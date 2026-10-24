---
atom_id: CA-R-1864@2
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 2
updated_at: 2026-10-23 01:47:30 +0400
subjects:
  governs: Subject/Engineering/Journal Event Query/Authorization Boundary
  depends_on:
  - Subject/Domain/Node/Continuant/History/Journal
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
relations:
  relates_to:
  - CA-O-162
  - CA-E-579
type: Rule
---
# Summary

Preserve Journal query read-only and secret boundaries

## Scope

The query authorization boundary.

## Claim

FIND_AND_FETCH_JOURNAL_EVENTS **must not** create mutation authority, read credentials or secrets, or evaluate arbitrary SQL or code.

## Details

Rejected inputs and redacted protected values are reported as boundaries, not fetched, logged, or transformed into authority.
