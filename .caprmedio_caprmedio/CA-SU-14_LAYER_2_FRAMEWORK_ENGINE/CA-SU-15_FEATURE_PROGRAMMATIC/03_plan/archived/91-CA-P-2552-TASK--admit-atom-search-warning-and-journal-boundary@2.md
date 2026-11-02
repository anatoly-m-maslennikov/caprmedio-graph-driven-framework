---
atom_id: CA-P-2552
content_role: Plan
type: Plan
label: Task
work_sequence_number: 91
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2401]
version: 2
updated_at: "2026-10-21T17:03:30Z"
---
# Summary

Admit the AtomSearch warning and Journal boundary

## Objective

Reconcile the Operator's warning disposition for individual schema-invalid Atoms
with the active ATOM_SEARCH, diagnostic-logging, and query-Journal authorities,
then obtain bounded implementation and focused proof without claiming deployment
or release conformance.

## Details

At most 15 minutes own work per child; split before extending. CA-C-572 is the
active source problem. An isolated schema-invalid Atom may be skipped with a
technical warning containing path and reason while a bounded scan continues with
`complete: false`; fatal I/O, security, duplicate-identity, stale, ambiguous, or
incomplete-frontier conditions remain refusal/error. Technical warnings go through
the configured runtime diagnostic logging authority and are not business Journal
records. Reuse CA-M-163, CA-D-396, CA-D-504 and CA-D-559 as logger authorities;
do not hard-code `.caprmedio_runtime/logs/` or choose a container-only sink while
the Operator's sink question is unanswered. Preserve historical Journal bytes and
the existing actual-query Run/Journal route. Root owns code, tests, Git, Docker,
runtime, and any release or deployment effect.

### Bounded decomposition

- CA-P-2553 is Done for the implementation/contract increment after the focused
  33-test AtomSearch check.
- CA-P-2554 is Done for the dependent focused proof; it preserves the
  source/test-only and no-deployment boundary.
- CA-P-2555 is Backlog and depends on CA-P-2553; it remains pending the explicit
  sink-policy answer and must not select a sink by inference.

This plan does not modify the frozen local-release carriers CA-R-1878, CA-M-332 or
CA-E-573, does not close CA-P-2536 or CA-P-2401, and does not claim the 33 focused
tests as installed-runtime or deployment proof.

### Definition of Done

The children provide exact source/test evidence for warning path/reason,
`complete: false`, no mutation, preserved Journal history, and fatal-class
refusal. The logger boundary is reconciled only after the configured sink decision
is answered. Until those observations exist, leave this Task Active and preserve
the unresolved CA-C-572 problem.
