---
atom_id: CA-R-1871
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Active
author: Anatoly Maslennikov
version: 8
updated_at: 2026-10-27 20:00:05 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
relations: {}
type: Rule
tier: 3
---
# Summary

Return observable query result and limit evidence

## Scope

The query result envelope.

## Claim

FIND_AND_FETCH_JOURNAL_EVENTS **must** return the snapshot token, result selection, pagination state, coverage state, and recoverable diagnostics sufficient to distinguish complete, partial, invalid, and blocked outcomes.

## Details

The envelope reports evidence and limits without exposing credentials, secrets, or unselected Event content.
