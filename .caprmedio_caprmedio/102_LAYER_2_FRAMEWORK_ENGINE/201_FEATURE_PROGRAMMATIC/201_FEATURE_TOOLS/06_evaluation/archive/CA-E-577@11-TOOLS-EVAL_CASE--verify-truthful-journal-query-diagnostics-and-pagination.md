---
atom_id: CA-E-577@11
content_role: Evaluation
type: Eval Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 11
updated_at: 2026-10-27 06:04:45 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Execution Control/Failure Handling
  depends_on:
  - Subject/Graph Node/Engineering/Data Handling/Source Retrieval
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Evaluation'
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
