---
atom_id: CA-E-673
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Active
author: Anatoly Maslennikov
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
version: 2
role: Evaluation
form: Eval Case
tier: 5
carrier_destination:
  file:
    name: CA-E-673-WORKBENCH-EVAL_CASE--align-mcp-run-check-and-web-results.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/06_evaluation
relations:
  evaluation_for: [CA-R-2729, CA-R-2727, CA-D-673, CA-D-674]
updated_at: 2026-11-04 00:38:14 +0400
---
## Summary

Align MCP Run, Check, and simple web query results

## Claim scope

Direct MCP and web results over one in-memory SQL connector.

## Claim

### Prose Claim

MCP Run, MCP Check, and the web page directly and synchronously invoke one in-memory SQL connector. They add no planner, scheduler, queue, Workflow, or job. Run returns the execution's complete rows, names, types, and counts; Check returns validity and exact counts or the query error. Hashes belong only to source-derived `atoms` and `scope_units` rows: an arbitrary result, including `SELECT COUNT(*)`, gains no hash column.

## Details

| Fixture | Expected outcome |
| --- | --- |
| Multi-row Run through MCP and web | Each direct request returns its own connector result before completion, with exact names, types, rows, and counts. |
| `SELECT COUNT(*) FROM atoms` | Only the requested aggregate column is returned. |
| Invalid SQL or oversized MCP result | The caller receives respectively its query error or explicit full-result delivery failure; no empty success or silent limit occurs. |
| Background source error | The indexer writes stderr and skips the source; the valid direct query result stays ordinary SQL data. |
