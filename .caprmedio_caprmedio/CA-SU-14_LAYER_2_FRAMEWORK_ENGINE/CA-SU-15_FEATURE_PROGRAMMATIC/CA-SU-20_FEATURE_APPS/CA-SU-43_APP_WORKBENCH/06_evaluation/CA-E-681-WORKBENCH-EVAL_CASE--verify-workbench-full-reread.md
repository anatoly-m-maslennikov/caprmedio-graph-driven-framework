---
atom_id: CA-E-681
role: Evaluation
form: Eval Case
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Active
version: 1
author: Anatoly Maslennikov
tier: 6
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations:
  evaluation_for:
  - CA-R-2786
  - CA-M-474
  - CA-D-679
updated_at: 2026-11-05 13:52:40 +0400
carrier_destination:
  file:
    name: CA-E-681-WORKBENCH-EVAL_CASE--verify-workbench-full-reread.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/06_evaluation
---

## Summary

Verify Workbench full reread

## Claim

The Workbench full reread recreates all derived state from the current governed sources, exposes the same operation through MCP and health, preserves source and saved items, and reports failure without automatic retry when a required source or startup step is invalid.

## Details

| Scenario | Expected outcome |
| --- | --- |
| Add a declared source property and run `workbench_reread({})` | The old database, WAL and temporary files are gone; the new schema contains the current columns and the source is read again. |
| Query after reread | Current Atom and Scope Unit rows, direct and derived relations, graph data and query results come from the rebuilt state; stale rows and columns are absent. |
| Existing saved query or Worksheet and source Journal | Both remain available; no source Journal record is deleted. |
| Existing query-result ID before reread | The ephemeral result is no longer available after the derived result tables are recreated. |
| MCP and health actions | Both invoke the same full-reread operation and expose the same ready or failure result; MCP remains usable. |
| `discover_tools` | `workbench_reread` appears under `Service`. No generic service registry is required. |
| Invalid Scope Unit Declaration | Reread fails explicitly and Workbench is not reported ready. No automatic retry or fallback to the old derived database occurs. |
| Invalid non-Declaration source | The existing reader error behavior is used; valid source handling is not replaced by stale derived data. |
