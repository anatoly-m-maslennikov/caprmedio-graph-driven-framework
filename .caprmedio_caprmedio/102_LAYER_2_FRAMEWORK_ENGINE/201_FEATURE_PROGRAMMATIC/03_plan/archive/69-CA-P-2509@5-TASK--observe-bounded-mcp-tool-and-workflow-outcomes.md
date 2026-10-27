---
atom_id: CA-P-2509@5
content_role: Plan
type: Plan
label: Task
work_sequence_number: 69
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Engineering/MCP
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2401
version: 5
updated_at: 2026-10-24 10:35:14 +0400
tier: 3
---
# Summary

Observe bounded MCP Tool and Workflow outcomes

## Objective

Capture recent real calls and Workflow observations at the existing Gateway boundary.

## Details

At most 15 minutes own work; split before extending. Depends on reviewed P2508. Own only bounded process-local observations and narrow Gateway hooks. Keep no more than 32 Tool observations and 32 Workflow observations, with since-start coverage explicit. Preserve returned domain outcome, uncertain no-replay behavior and separate scheduler status from actual Workflow outcome. No raw arguments/results, paths, credentials or provider exception text. Acceptance: truthful success/rejection/error/uncertain and empty/eviction cases; no redispatch or DBOS/Docker query from health.

### Dependency review before implementation

P2508 contract review is complete; R2007/E640/D639 are Active. Own health_observations.py and narrow hot_reload.py hooks exclusively. The shared API is HealthObservations.record(name, arguments, response, error=None, started_at=None) and snapshot(), exposed as gateway.health_observations. Snapshot contains started_at, calls and workflows, with no raw data. Expose safe inner exception categories without changing the public Tool result; concurrency must not mix records. Coordinate the exact minimal API with the page/test owners before execution. Root owns planning, canonical Source changes, Git/index and release.

### Verified checkpoint and dependent review

Implemented bounded process-local Tool/Workflow observations, cancellation uncertainty and validated actual-Workflow identity gating. Every Workflow RPC still has a Tool row; Action/Step/coordinator outcomes cannot masquerade as Workflow outcomes. Final root gate passed18 health tests in15.581s,21 existing hot-reload tests in67.027s and7 existing HTTP tests in16.508s. Before/after health source/test hashes match. Observer and HTTP independent reviews APPROVE. P2511 reviewed the frozen inputs before final acceptance; no deployed-state or complete-history claim.
