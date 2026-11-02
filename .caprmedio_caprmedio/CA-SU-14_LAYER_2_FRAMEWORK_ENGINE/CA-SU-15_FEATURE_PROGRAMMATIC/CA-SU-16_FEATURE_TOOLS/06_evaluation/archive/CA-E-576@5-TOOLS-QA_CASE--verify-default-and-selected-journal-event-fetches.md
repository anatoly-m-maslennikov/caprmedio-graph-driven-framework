---
atom_id: CA-E-576@5
content_role: Evaluation
type: Eval Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 5
updated_at: 2026-10-24 05:41:48 +0400
subjects:
  governs: Subject/Domain/Node/Continuant/History/Journal.Record
  depends_on:
  - Subject/Engineering/Journal Event Query
  - Event
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Evaluation'
relations:
  evaluation_for:
  - CA-R-1863
tier: 4
---
# Summary

Verify default and selected Journal Event fetches

## Claim

The Tool returns only Event IDs by default and returns only explicitly selected fields or full Events when requested.

## Test case

Query one snapshot in default, selected-field, full-Event, and missing-selected-field modes.

## Acceptance criteria

Default records contain only canonical IDs; selected mode preserves requested field order; full mode preserves Event content; missing values remain explicit diagnostics.

## Failure disposition

Reject unrequested Event content, filename IDs, or synthesized missing values.
