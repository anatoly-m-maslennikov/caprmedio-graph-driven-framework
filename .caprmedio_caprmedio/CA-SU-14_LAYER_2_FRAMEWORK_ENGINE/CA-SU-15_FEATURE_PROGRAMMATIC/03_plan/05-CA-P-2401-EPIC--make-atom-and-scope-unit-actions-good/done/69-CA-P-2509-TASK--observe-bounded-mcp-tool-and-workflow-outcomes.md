---
atom_id: CA-P-2509
ref_id: CA-P-2509
container:
  atom: CA-P-2401
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Engineering/MCP
tier: 3
relations:
  is_decomposition_of:
  - CA-P-2401
status: Done
version: 6
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 69-CA-P-2509-TASK--observe-bounded-mcp-tool-and-workflow-outcomes.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/03_plan/5-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/done
work_sequence_number: 69
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
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
