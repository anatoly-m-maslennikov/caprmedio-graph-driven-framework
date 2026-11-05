---
atom_id: CA-E-783
ref_id: CA-E-783
container:
  scope_unit: CA-SU-46
role: Evaluation
form: Eval Case
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
tier: 5
relations:
  evaluation_for:
  - CA-R-2727
  - CA-D-674
status: Archived
version: 1
updated_at: 2026-11-05 20:34:04 +0400
carrier_destination:
  file:
    name: CA-E-783@1-WORKBENCH_FRONTEND-EVAL_CASE--verify-result-display-preferences.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-46_FEATURE_WORKBENCH_FRONTEND/06_evaluation/archive
current_scope_unit: WORKBENCH_FRONTEND
claim_target_scope_unit: WORKBENCH_FRONTEND
author: Anatoly Maslennikov
---

## Summary

Verify Workbench result-display preferences

## Claim scope

The Workbench frontend's result sizing and content presentation remain user-controlled, persisted, and query-stable.

## Claim

In a fresh browser context, verify Theme = System, Text zoom = 100% and Interface zoom = 100%, alongside the specified embedded/standalone density defaults.

### Prose Claim

A real-browser evaluation **must**:

- begin with a query result large enough to exercise paging and a value longer than 150 Unicode characters. With no saved preference, Results show Adaptive row sizing and Limited content up to N=150; the retained Fixed value is 100 and its numeric field is not shown until Fixed is selected.
- switch Settings to Fixed, confirm the retained 100-row value is shown, enter a positive integer page size within 1..1000, reload, and confirm the selected value and displayed page size persist. Values outside the existing 1..1000 page-size boundary are rejected without changing the previous valid choice; returning to Adaptive hides the Fixed numeric field.
- switch to Adaptive and confirm the visible Results fit the available area. Resize the browser and change Text zoom, Interface zoom and Density; the displayed page size adapts without losing the current query result.
- navigate to another page after a display-only change and confirm the existing query_id/page flow is reused and SQL is not run again.
- use the inline ResultsTable header control to switch between Limited and Full, reload, and confirm the preference persists. Limited mode accepts any positive integer N (150 by default) and displays exactly the first N Unicode characters; the N field is hidden when Full is selected, while the complete returned value remains unchanged for the query/MCP result.
- exercise the same result-display actions from Settings, the ResultsTable header and the command palette, confirming they produce one consistent persisted preference rather than divergent controls.
- confirm the result grid is read-only with no cell or row editor. Its context menu exposes only Cell Copy value, Cell Show full value, Row Copy row, Column Sort ascending, Column Sort descending, Group by, Filter and Clear filter; these actions preserve the full result and do not rerun the current View query.

The evaluation passes only when the browser-visible behavior meets every case and no presentation change causes a new SQL execution.

