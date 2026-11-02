---
atom_id: CA-E-579@2
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 2
updated_at: 2026-10-23 03:14:50 +0400
subjects:
  governs: FIND_AND_FETCH_JOURNAL_EVENTS/authorization boundary
  depends_on:
  - Tool
  - Subject/Engineering/Journal Event Query
  - Evaluation
relations:
  evaluation_for:
  - CA-R-1864
---
# Summary

Verify Journal query read-only and secret exclusion

## Claim

The Tool rejects mutation, credential, secret, arbitrary SQL, and arbitrary-code requests without reading protected values or changing Journal data.

## Test case

Submit each forbidden parameter against a before/after Journal digest and protected-value sentinel.

## Acceptance criteria

Each request is rejected with a boundary diagnostic; the Journal digest and sentinel access count are unchanged.

## Failure disposition

Reject any mutation authority, protected-value read, or executable interpretation.
