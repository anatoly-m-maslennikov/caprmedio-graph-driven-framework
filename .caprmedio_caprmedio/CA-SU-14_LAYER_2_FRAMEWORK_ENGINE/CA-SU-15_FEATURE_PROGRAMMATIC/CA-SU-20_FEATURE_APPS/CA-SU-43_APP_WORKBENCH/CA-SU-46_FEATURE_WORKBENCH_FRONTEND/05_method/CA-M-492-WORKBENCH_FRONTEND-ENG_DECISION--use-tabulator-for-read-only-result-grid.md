---
atom_id: CA-M-492
ref_id: CA-M-492
container:
  scope_unit: CA-SU-46
role: Method
form: Eng Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
tier: 4
relations:
  method_for:
  - CA-D-674
status: Active
version: 1
updated_at: 2026-11-05 20:34:04 +0400
carrier_destination:
  file:
    name: CA-M-492-WORKBENCH_FRONTEND-ENG_DECISION--use-tabulator-for-the-workbench-read-only-result-grid.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-46_FEATURE_WORKBENCH_FRONTEND/05_method
current_scope_unit: WORKBENCH_FRONTEND
claim_target_scope_unit: WORKBENCH_FRONTEND
author: Anatoly Maslennikov
---

## Summary

Use Tabulator for the Workbench read-only result grid

## Claim scope

Workbench frontend result-grid presentation and interaction.

## Claim

### Prose Claim

Use Tabulator 6.7.1 directly in the Svelte frontend as the Workbench result grid. Do not add a wrapper framework or a second grid engine. Keep the grid read-only: provide no cell or row editors and do not turn grid actions into mutations.

Use the existing backend Workbench View/grid/page contract against the complete materialized cached result. Backend filtering, multisort, one-column grouping and exact global row/group counts apply to the whole cached result, not only to the currently loaded page; the frontend consumes page slices and does not rerun the View query for display actions. Preserve one View as one query and use the same backend View context in standalone and embedded Workbench modes.

Expose only the approved read-only context actions: Cell Copy value, Cell Show full value, Row Copy row, Column Sort ascending, Column Sort descending, Group by, Filter and Clear filter. Group by is limited to one column in this MVP. Preserve positional columns, duplicate labels and dotted labels. Do not add nested grouping, pivoting, exports, collaboration, editors or persisted grid state. The Adaptive/Fixed row preference and Full/Limited content preference remain presentation-only; the full cached rows and values stay unchanged.

### Sources

- [Tabulator 6.x documentation](https://www.tabulator.info/docs/6.x)
- [Tabulator 6.x MIT license](https://www.tabulator.info/docs/6.x/license)

