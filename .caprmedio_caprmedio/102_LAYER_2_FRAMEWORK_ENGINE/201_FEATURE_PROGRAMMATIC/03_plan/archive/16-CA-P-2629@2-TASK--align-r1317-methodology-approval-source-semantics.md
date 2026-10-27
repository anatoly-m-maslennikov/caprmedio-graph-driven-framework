---
atom_id: CA-P-2629@2
content_role: Plan
type: Plan
label: Task
work_sequence_number: 16
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Archived
version: 2
updated_at: 2026-10-23T13:10:12+0400
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2613
  depends_on:
  - CA-C-585
  - CA-C-583
  - CA-P-2622
  relates_to:
  - CA-R-1317
  - CA-O-007
  - CA-O-155
  - CA-O-156
  - CA-R-1525
  - CA-R-1720
  - CA-D-340
---
# Summary

Align R1317 methodology-approval source semantics

## Objective

Prepare and review the smallest explicit source alignment for R1317, O007,
O155 and O156 after the Operator's decision that Journal recording is
non-blocking for methodology approvals and recovery. Preserve the requirement
for an actual OperatorDecision plus independent Run/effect evidence.

## Details

This is one bounded source-reconciliation Task with at most 15 minutes of own
work. Apply the resolved CA-C-585 boundary to the six current clauses under
CA-C-583 without turning a business Journal append into generic permission,
completion or recovery proof. Keep O130/O131 and the four graph clauses at
their current versions until the source review passes; the current O130/O131
writer successors are still under review. Preserve exact source IDs, versions,
paths and predecessor history. Do not invent a caller-supplied approval flag,
change compiler behavior, mutate live bindings or run release/deployment.

## Definition of Done

Return the reviewed source diff or a precise bounded proposal for R1317,
O007, O155 and O156, with the non-blocking Journal boundary and independent
decision/Run/effect evidence stated explicitly. Record unresolved review of
the remaining current clauses. Do not mark CA-C-583 resolved or unblock
CA-P-2620/CA-P-2621 until all six clauses and their current versions pass
review.

## Independent source-review completion — 23 October 2026

The four scoped current methodology carriers passed independent review at
99% or higher. The accepted current pins are:

| Atom | Version | SHA-256 |
| --- | ---: | --- |
| CA-R-1317 | 18 | 7eca1569caf1e9442c6b116e5b3ce2a0da2fd4049e97115f9ac72b8b415c46a2 |
| CA-O-007 | 14 | 208e2665922bc4948d8e6f6780eeec36a660c6dc8d59581ae70e94959345ed70 |
| CA-O-155 | 10 | 084318013d9192c049ca163b94bee872f1e47056b9f7d22c4687e5216cf0934a |
| CA-O-156 | 11 | 5eb7eb70aacdd09c05f118b8246e9d994a9a9a1887a31ec050b16b2f76446193 |

The source alignment preserves a non-blocking Journal recording obligation,
while requiring an actual OperatorDecision and independently verified Run and
effect evidence. This Task is Done for the four-carrier source package. The
compiler/shared-run RMED reconciliation remains in CA-P-2631; CA-P-2630
remains Backlog while that reconciliation and the open CA-C-586 O011 decision
hold. CA-C-583 remains Active for the remaining implementation boundary. No
code, binding, runtime, release or deployment change is claimed here.
