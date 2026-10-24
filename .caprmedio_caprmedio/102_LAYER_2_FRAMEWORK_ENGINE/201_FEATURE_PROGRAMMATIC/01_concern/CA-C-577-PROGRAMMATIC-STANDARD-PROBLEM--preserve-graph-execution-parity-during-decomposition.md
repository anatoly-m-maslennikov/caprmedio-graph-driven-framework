---
atom_id: CA-C-577
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Resolved
priority: high
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  concern_about: [CA-P-2589, CA-P-2590, CA-P-2595, CA-E-539, CA-E-540, CA-M-403, CA-M-405]
version: 2
updated_at: "2026-10-22T11:38:21Z"
---
# Summary

Preserve graph execution parity during decomposition

## Concern

Independent read-only review of the unaccepted four-module graph-loop extraction found a recovery regression: build_action_context checks membership in session.actual after start_run has inserted the new Action. A newly started change_atom_status Action during recovery is therefore incorrectly treated as restored and returns lifecycle-recovery-required rather than performing the admitted first execution. The predecessor snapshots actual Run identities before any starts. The current working-tree executor delegates to this extraction, so passing the one-Step happy-path smoke is not refactor acceptance.

The same review found execute_graph still owning visit control, dispatch, retained-state mutation and both completion paths in one oversized executable unit; retain_prior_result accepts an opaque nine-value Any varargs packet; and three exact writer diagnostics plus the non-string terminal error drifted from their predecessor. Source file-size, Ruff and Mypy successes do not discharge these behavioral and cohesion findings.

## Required disposition

Repair the extracted canonical owners without new business rules or an exception. Capture restored identities at entry, preserve genuine restored versus newly started recovery behavior, use explicit typed result-retention arguments, retain exact diagnostics and split the remaining oversized traversal unit by real responsibility. Add focused recovery, multi-Step/revisit and diagnostic parity checks. Re-run the related preserved legacy portfolio and independent review against exact current source bytes before CA-P-2590 and CA-P-2595 can complete.

Do not bypass the findings with class-wrapper result normalization, untyped self proxies, a generic registry, broader suppression, rewritten frozen source data or a claimed passing gate. Current shared-context features remain paused. CA-P-2589 owns the repair; the original executor and production caller integration remain under one writer.

## Resolution — 22 October 2026

The canonical extraction now snapshots restored Action identities before any starts, distinguishes new and genuinely restored Actions, retains exact creation/lifecycle/replacement writer and terminal diagnostics, and uses explicit typed prior-result arguments. Traversal responsibilities are cohesive and bounded. Independent review subsequently found and closed one further parity difference: graph projections again perform the unconditional final write after Step and Workflow terminal attempts, including unconfirmed receipts.

Four durable tests in test_selected_graph_recovery_parity.py cover recovery membership, frozen O016 revisit identities/order, exact diagnostics and the final projection write trace. Six related focused legacy checks, strict Mypy and pinned Ruff format/lint/C901 passed for the owned graph lane. Independent source/assertion review returned PASS. No source-size exception or current Workflow feature was introduced.

This resolves the identified graph extraction findings only. Public executor integration, manifest-fixture isolation and Subject-batch caller closure remain subject to CA-P-2590 and CA-P-2595; the separate Integrated continuation gap CA-C-576 remains Active.

## Evidence boundary

These findings concern unaccepted local refactoring, not a deployed incident or a new Workflow policy. Agent and selected-route refactors have separate reviewed acceptance. Current Integrated continuation remains a distinct implementation gap in CA-C-576. No full suite, production MCP traffic, release, deployment or uncertain replay was used to claim graph-loop acceptance.
