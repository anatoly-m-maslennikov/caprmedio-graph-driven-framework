---
atom_id: CA-P-2630
content_role: Plan
type: Plan
label: Task
work_sequence_number: 17
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Backlog
version: 1
updated_at: "2026-10-23T12:54:02+0400"
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2613]
  depends_on: [CA-P-2623, CA-P-2629, CA-C-585]
  relates_to: [CA-O-016, CA-R-1317, CA-O-007, CA-O-155, CA-O-156, CA-C-583]
---
# Summary

Define the compiler admitted-evidence contract

## Objective

Define the smallest compiler implementation contract that consumes existing
admitted OperatorDecision, Run and effect evidence, while treating Journal
recording as non-blocking for methodology approvals and recovery. The contract
must not accept an authoritative approval flag supplied by the caller.

## Details

This is one bounded contract-design Task with at most 15 minutes of own work,
to activate after CA-P-2629's source alignment is reviewed. Identify the
existing evidence carriers and current compiler callers, preserve result
shapes, partial results, retry accounting, recording_error handling and
no-replay behavior, and separate business Journal append from technical
diagnostics. Do not invent a new input schema, alter source Atoms, or change
runtime behavior in this planning record. Failed-publication recovery evidence
remains separately unresolved until its current source is adjudicated.

## Definition of Done

Return a source-bound contract proposal naming the admitted evidence fields,
their owner and freshness checks, the caller-visible failure/partial-result
behavior and focused regression boundaries. The proposal must reject a
caller-authoritative approval flag and must not claim CA-C-583 resolved or
runtime/compiler implementation complete. Activate only after CA-P-2629 is
reviewed.
