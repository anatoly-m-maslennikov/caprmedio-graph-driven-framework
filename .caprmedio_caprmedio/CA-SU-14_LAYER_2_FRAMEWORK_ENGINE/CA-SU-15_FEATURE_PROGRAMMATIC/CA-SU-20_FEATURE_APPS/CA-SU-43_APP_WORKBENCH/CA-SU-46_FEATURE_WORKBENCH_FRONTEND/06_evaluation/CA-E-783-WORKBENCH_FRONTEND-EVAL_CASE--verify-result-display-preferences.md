---
identity:
  atom_id: CA-E-783
  ref_id: CA-E-783
context:
  container:
    scope_unit: CA-SU-46
  role: Evaluation
  form: Eval Case
  topics:
    main_subject: MODEL//CAPRMEDIO <+ Projection
  tier: 5
relations:
  evaluation_for:
  - CA-R-2727
  - CA-D-674
state:
  status: Active
  version: 6
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-E-783-WORKBENCH_FRONTEND-EVAL_CASE--verify-result-display-preferences.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-46_FEATURE_WORKBENCH_FRONTEND/06_evaluation
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

In a real browser, start with a paged result and value over 150 Unicode characters. Defaults are Adaptive rows and Limited N=150; Fixed retains 100 and reveals its numeric field only when selected. Fixed accepts persisted positive 1..1000 page size; invalid values preserve prior choice, and Adaptive hides the field/fits available area through resize and all zoom/Density changes without losing result. Display-only changes and later pages reuse query ID/page flow without rerunning SQL.

Limited/Full is one persisted canonical preference available from Settings, ResultsTable header and palette. Limited displays exactly first positive-N Unicode characters; Full hides N while returned value remains whole. Verify Dark readable names/muted types and Tabulator states, pre-wrap every source newline, and cached-result resize/grid leave/rebuild without uncaught delayed callback. CA-E-786 owns exact action matrix/one-column grouping/global cache semantics. Pass only with browser-visible preference persistence, query stability and no uncaught error.
