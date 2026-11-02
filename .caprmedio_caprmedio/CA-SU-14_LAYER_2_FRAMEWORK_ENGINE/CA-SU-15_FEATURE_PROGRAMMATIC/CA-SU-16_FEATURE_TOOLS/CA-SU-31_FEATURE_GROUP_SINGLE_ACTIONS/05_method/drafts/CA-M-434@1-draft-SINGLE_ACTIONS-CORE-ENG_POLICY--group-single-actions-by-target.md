---
atom_id: CA-M-434@1-draft
content_role: Method
type: Eng Policy
current_scope_unit: SINGLE_ACTIONS
claim_target_scope_unit: SINGLE_ACTIONS
tier: 1
status: Draft
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-23 18:22:28 +0400"
subjects:
  governs: "Subject/Engineering/Target-Specific Tool Operations"
  depends_on: []
---
# Summary

Group Single Actions by target

## Scope

The target and operation boundaries of the SINGLE_ACTIONS Tool group.

## Claim

Keep six distinct target children under SINGLE_ACTIONS:
`ATOM_ACTIONS`, `SCOPE_UNIT_ACTIONS`, `PROJECTION_ACTIONS`,
`JOURNAL_ACTIONS`, `PROJECT_ACTIONS`, and `QUEUE_ACTIONS`. Put the target
first, then its supported operations. Find chooses matches, Fetch returns
content, and Check does not mutate. Create, Update, and other operations stay
specific to the target rather than being forced into uniform CRUD. A status
change is part of Update, not a standalone operation.

## Details

- `JOURNAL_ACTIONS` supports only Find, Fetch, and Append.
- `PROJECTION_ACTIONS` supports Find, Fetch, Create, and Update/Rebuild.
- `QUEUE_ACTIONS` supports Find for queued/running jobs, Fetch for status/results,
  Enqueue, cancellation of pending work, and pause/resume of dispatch.
  Its direct queue-control path is not queued on
  a paused queue, and pausing does not cancel running work.

Other target groups expose only meaningful supported operations; do not invent
a complete target-operation matrix. Governing Configuration belongs to
ADAPTERS, not to this target group.
