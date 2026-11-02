---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Graph Node/Domain/Continuant/History/Journal.Record
  depends_on:
  - Subject/Graph Node/Engineering/Execution Control/Failure Handling
  - Subject/Graph Node/Carrier
  - Subject/Graph Node/Domain/Continuant/Project
  - Subject/Graph Node/Carrier/Git Index
  - Subject/Graph Node/Implementation/Code/Tool//COMMIT_CONTEXT
version: 12
updated_at: 2026-10-27 06:04:45 +0400
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CA-R-1491
  - CA-M-087
  - CA-R-804
  - CA-R-812
atom_id: CA-E-479@12
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 3
---
# Preserve intact historical events during safe append

## Claim checked

APPEND_CHANGE_RECORDS rejects a damaged sealed event envelope **or** an unsafe append attempt, **not** intact historical evidence merely because the live Project changed.

## Cases

1. gather a sealed event **and** alter a sealed observation field **without** updating its integrity binding.
2. attempt an append against a Journal position invalidated by another accepted append.
3. retain the intact historical event **and** independently advance the Project's Git base **or** change its observed subject **after** capture.

## Acceptance

- case 1 fails event-integrity checks **before** append; the Doer **must not** silently reseal changed facts.
- case 2 obtains a current safe append position **or** returns a storage-conflict result **without** partial append, loss of the pending event, **or** rewritten history.
- case 3 remains recordable as the original historical observation. it does **not** authorize a Project mutation against stale preconditions.
- failed append attempts release unconsumed storage leases **and** preserve the exact pending event for admitted retry.

## Failure disposition

reject the appender Implementation **if** it accepts damaged event data, overwrites accepted records, drops historical evidence because of later Project changes, **or** treats Journal admission as Git mutation approval.
