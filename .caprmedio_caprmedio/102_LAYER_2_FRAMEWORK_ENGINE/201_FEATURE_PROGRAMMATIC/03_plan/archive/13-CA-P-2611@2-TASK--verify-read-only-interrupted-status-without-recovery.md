---
atom_id: CA-P-2611@2
content_role: Plan
type: Plan
label: Task
work_sequence_number: 13
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Archived
version: 2
updated_at: '2026-10-22T19:51:48Z'
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2581
  depends_on:
  - CA-P-2601
  relates_to:
  - CA-O-016
  - CA-C-582
---
# Summary

Verify read-only interrupted status without recovery or replay

## Objective

Verify the public read-only status and recovery boundary after an accepted
terminal/interrupted_pending result. Preserve the canonical graph result,
make the explicit recovery requirement observable, and prove that status
inspection does not mutate the Run or replay completed Actions.

## Details

One Task per file; at most 15 minutes of own work. Split before expanding.
Review and update dependent Tasks after the observed result and before
execution. Use the current PROGRAMMATIC M/E/D guidance, the locked uv
environment and the bounded source-bound fixture. Preserve exact prior
receipts, source pins, Project identity, partial-result visibility and
business-only Journal semantics. Record the read-only storage/API boundary
owned by the checkpoint worker; root owns observation integration. Create a
Concern for a new blocker. No production MCP traffic, Docker action,
full-suite run, release, deployment, uncertain replay or Git publication.

## Definition of Done

Against frozen nonproduction inputs, assert the exact canonical terminal and
interrupted_pending fields, the corresponding graph_result, the final public
status and its recovery message. Confirm that read-only status and recovery
inspection preserve the existing Run root, do not replay completed Actions,
and do not invent a successful completion. Keep current Project binding,
runtime admission and handoff as separate gates.

### Accepted completion evidence — 22 October 2026

The bounded read-only status/recovery verification passed: 64/64 focused integrated-action checks, six direct observation guards and seven checkpoint checks; strict SDK journey 4/4 in 30.110s with exact terminal/interrupted_pending state, final public status and verified graph-result bytes; final Docker-free stdio smoke with 23 tools; Ruff and mypy passed. The status path preserves the canonical interrupted state without granting recovery permission, replaying completed Actions or inventing completion. No production, release or deployment claim is made.
