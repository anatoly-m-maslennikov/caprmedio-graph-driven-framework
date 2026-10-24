---
atom_id: CA-E-544
content_role: Evaluation
type: Eval Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Active
author: Anatoly Maslennikov
version: 8
updated_at: 2026-10-24 04:47:50 +0400
subjects:
  governs: Subject/Engineering/Journal Operations
  depends_on:
  - Subject/Domain/Node/Continuant/History/Journal
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Evaluation'
relations:
  evaluation_for:
  - CA-R-1824
tier: 4
---
# Summary

Verify selected Run Journal retry without effect replay

## Scope

Storage recovery of a terminal selected-Run event after its domain effect has
already occurred.

## Claim

When recording retry is supported, an append failure retains identical pending
evidence and a retry appends without rerunning its completed Action. Neither
receipt nor canonical-once recovery is a mutation-success gate.

## Test case

Run a golden terminal Action once and capture its immutable event bytes,
Event ID, effect counter, and sealed append context (author, local date,
timezone, original partition). Inject a crash/failure after the event fsyncs
but before its receipt is persisted. Restart with a later local date/timezone
context and retry the original pending evidence. Then attempt changed bytes
under the same Event ID, including through a different date partition.

## Acceptance criteria

- The post-fsync/pre-receipt ambiguity preserves or reconstructs one canonical
  original event and its append context; it does not create a second append
  because the receipt was missing at crash time.
- The restart/date-rollover retry reuses the original author, local date,
  timezone, and partition context. It produces or reconciles exactly one
  canonical receipt for exactly one event and leaves the effect counter at one.
- A global Event-ID lookup finds that original receipt/history across
  partitions. Changed bytes under the same ID fail without overwriting Journal
  bytes, receipt, append context, or pending original, even when the current
  date would select another partition.
- No recovery path invokes the Action executor, dispatches a Step, creates a
  Run, or resets authorization. A separately admissible recovery Event retains
  a distinct identity and cannot replace the original terminal payload.
- Derived log views expose incomplete coverage before durable append and one
  canonical event after it.

## Details

Fault injection occurs at the append boundary only. The Action effect counter,
original event bytes, sealed append context, partition history, and receipt are
independent observations throughout recovery. The checked assertion is the
Claim above.

## Failure disposition

Reject duplicate or cross-partition appends, lost original context/pending
evidence, receipt ambiguity treated as a new event, byte overwrite, invented
recovery facts, or any Action replay caused by storage recovery.
