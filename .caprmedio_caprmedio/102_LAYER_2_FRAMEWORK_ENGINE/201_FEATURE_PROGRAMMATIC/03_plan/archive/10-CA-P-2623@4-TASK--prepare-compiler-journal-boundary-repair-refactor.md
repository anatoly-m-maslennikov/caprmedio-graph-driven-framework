---
atom_id: CA-P-2623@4
content_role: Plan
type: Plan
label: Task
work_sequence_number: 10
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Archived
version: 4
updated_at: 2026-10-24 06:04:43 +0400
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2613
  depends_on:
  - CA-C-583
  - CA-P-2622
  relates_to:
  - CA-O-016
  - CA-O-155
  - CA-O-156
  - CA-O-007
  - CA-R-1525
  - CA-R-1720
  - CA-D-340
  - CA-C-585
  - CA-P-2629
  - CA-P-2630
tier: 3
---
# Summary

Prepare the compiler journal-boundary repair refactor

## Objective

Prepare the smallest implementation/refactor boundary for the compiler and shared-run paths implicated by CA-C-583, without changing code in this planning Task. Keep business Journal recording, approval construction, failed-publication recovery and technical recording errors explicit and independently observable.

## Details

This is one preparation Task with at most 15 minutes of own work. Consume the accepted source-reconciliation proposal from CA-P-2622, identify the exact modules/functions and compatibility callers, and separate any implementation, refactor and test work that cannot fit one bounded Task. Preserve existing result shapes, partial results, retry accounting, no-replay behavior and the distinction between a real runtime fault and an invalid project artifact. Do not edit source code, tests, RMED, A1142, manifests, projections or runtime state. No live MCP, release, deployment, replay or full-suite run.

## Definition of Done

Return a concise refactor/repair plan with affected modules, preserved contracts, focused verifier commands and explicit follow-up Task boundaries. Do not claim CA-C-583 resolved or unblock CA-P-2620/CA-P-2621 from preparation alone.

### Compiler adjudication checkpoint — 23 October 2026

The Operator resolved CA-C-585: Journal recording is non-blocking for
methodology approvals and recovery; actual OperatorDecision and independent
Run/effect evidence remain required. The compiler contract must consume those
existing admitted evidence carriers and must not treat a caller-supplied
approval flag as authoritative. Source alignment for R1317, O007, O155 and
O156 is tracked by CA-P-2629; the compiler contract proposal is tracked by
CA-P-2630. Failed-publication recovery evidence remains separately unresolved.
No source-code or test change is authorized by this planning checkpoint.
