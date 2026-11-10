---
identity:
  atom_id: CA-E-783
  ref_id: CA-E-783@5
context:
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
state:
  status: Archived
  version: 5
  updated_at: 2026-11-09 07:45:14 +0400
destination:
  file:
    name: CA-E-783@5-WORKBENCH_FRONTEND-EVAL_CASE--verify-result-display-preferences.md
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

### Prose Claim

A real-browser evaluation must:

- begin with a query result large enough to exercise paging and a value longer than 150 Unicode characters. With no saved preference, Results use Adaptive row sizing and Limited content up to N=150; the retained Fixed value is 100 and its numeric field is not shown until Fixed is selected.
- switch Settings to Fixed, confirm that the retained 100-row value is shown, enter a positive integer page size within 1..1000, reload, and confirm that the selected mode and page size persist. Values outside the existing 1..1000 boundary are rejected without changing the previous valid choice. Returning to Adaptive hides the Fixed numeric field.
- switch to Adaptive and confirm that visible Results fit the available area. Resize the browser and change Interface text zoom, Content text zoom, whole-Interface zoom and Density; the displayed page size adapts without losing the current query result.
- navigate to another page after a display-only change and confirm that the existing query_id/page flow is reused and SQL is not run again.
- use the inline ResultsTable header control to switch between Limited and Full, reload, and confirm the preference persists. Limited accepts any positive integer N, with N=150 as the default, and displays exactly the first N Unicode characters. The N field is hidden when Full is selected, while the complete returned value remains unchanged for the query/MCP result.
- exercise the same result-display actions from Settings, the ResultsTable header and the command palette, confirming one consistent persisted preference and one canonical handler rather than divergent controls.
- switch to Dark theme and confirm result names remain prominent, SQL types/formats remain smaller and pale, and Tabulator headers, cells, borders and hover/focus/selected states remain readable.
- confirm Content cells and full-value views render every source newline as a visible line break with pre-wrap presentation, without requiring a blank line or collapsing a single newline into a space.
- open a View with an already-cached result, let Adaptive sizing fetch its page, then resize, change the grid and leave or rebuild the result. Capture uncaught browser errors throughout these actions; no delayed grid callback may update a destroyed instance.

The exact read-only result-grid action matrix, editor prohibition, one-column grouping and global cached-result filter/sort/group behavior are evaluated by CA-E-786 and are not repeated here. The evaluation passes only when every display-preference case above is browser-visible, presentation changes do not cause a new SQL execution, preference persistence is truthful, and no uncaught browser exception occurs.
