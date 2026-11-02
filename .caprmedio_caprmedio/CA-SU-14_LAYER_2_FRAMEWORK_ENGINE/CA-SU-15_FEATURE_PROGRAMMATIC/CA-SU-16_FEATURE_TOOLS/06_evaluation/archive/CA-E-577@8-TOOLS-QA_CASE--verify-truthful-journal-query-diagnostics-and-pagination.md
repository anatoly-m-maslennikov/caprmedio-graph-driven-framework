---
atom_id: CA-E-577@8
content_role: Evaluation
type: Eval Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 8
updated_at: 2026-10-24 04:47:50 +0400
subjects:
  governs: Subject/Engineering/Tool/FIND_AND_FETCH_JOURNAL_EVENTS/diagnostics
  depends_on:
  - Subject/Engineering/Tool//FIND_AND_FETCH_JOURNAL_EVENTS
  - Subject/Engineering/Journal Event Query
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Evaluation'
relations:
  evaluation_for:
  - CA-R-1865
  - CA-R-1871
tier: 4
---
# Summary

Verify truthful Journal query diagnostics and pagination

## Claim

The Tool reports malformed Events, missing IDs, duplicate fields, incomplete reads, source changes, coverage, and page limits without silently skipping them.

## Test case

Introduce fixtures for raw duplicate JSON object keys before parsing, duplicate
Event IDs across captured members, malformed/missing-ID/incomplete reads,
frontier-member/per-member-byte/total-read exhaustion, and a bounded multi-page
snapshot. Continue after changed, deleted, truncated, unreadable captured
members and after an append outside the sealed prefix.

## Acceptance criteria

Every rejection identifies its exact diagnostic and configured/consumed limit
evidence; changed, deleted, truncated, or unreadable captured members reject
continuation, while append after the sealed prefix preserves it. No affected
fixture is reported complete.

## Failure disposition

Reject silent omission, invented completeness, or pagination across an unbound frontier.
