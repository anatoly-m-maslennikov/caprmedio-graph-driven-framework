---
atom_id: CA-E-578@10
content_role: Evaluation
type: Eval Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 10
updated_at: 2026-10-25 17:32:27 +0400
subjects:
  governs: Subject/Graph Node/Domain/Continuant/History/Journal.Record
  depends_on:
  - Subject/Graph Node/Engineering/Journal Event Query
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  - Subject/Graph Node/Domain/Occurrent/Execution/Action Run
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Evaluation'
relations:
  evaluation_for:
  - CA-R-1866
tier: 4
---
# Summary

Verify query snapshot excludes its own execution Events

## Claim

The Tool's result frontier remains unchanged when shared Run evidence appends during its actual invocation.

## Test case

Capture the Journal byte-prefix before workflow/action-start recording, start an
admitted execute invocation that records actual Run evidence, and append an
unrelated later Event before result pagination.

## Acceptance criteria

Returned IDs and continuation remain exactly the pre-dispatch snapshot; own and
later Events are absent, the result exposes the initial token and prefix hash,
and a standalone Action performs the same capture before its Run evidence.

## Failure disposition

Reject self-inclusion, frontier growth, or an unreported source change.
