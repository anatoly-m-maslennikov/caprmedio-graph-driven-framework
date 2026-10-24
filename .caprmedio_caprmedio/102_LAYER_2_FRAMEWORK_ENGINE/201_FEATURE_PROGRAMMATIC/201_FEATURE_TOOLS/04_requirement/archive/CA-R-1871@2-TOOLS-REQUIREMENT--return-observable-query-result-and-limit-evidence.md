---
atom_id: CA-R-1871@2
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
  governs: Subject/Domain/Node/Continuant/History/Journal.Record
  depends_on:
  - Subject/Domain/Node/Continuant/History/Journal
  - Subject/Engineering/Journal Event Query/Result Envelope
relations:
  relates_to:
  - CA-R-1865
  - CA-E-577
type: Rule
---
# Summary

Return observable query result and limit evidence

## Scope

The query result envelope.

## Claim

FIND_AND_FETCH_JOURNAL_EVENTS **must** return the snapshot token, result selection, pagination state, coverage state, and recoverable diagnostics sufficient to distinguish complete, partial, invalid, and blocked outcomes.

## Details

The envelope reports evidence and limits without exposing credentials, secrets, or unselected Event content.
