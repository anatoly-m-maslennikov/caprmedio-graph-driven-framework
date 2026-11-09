---
identity:
  atom_id: CA-E-786
  ref_id: CA-E-786
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
  - CA-M-492
  - CA-D-674
state:
  status: Active
  version: 3
  updated_at: 2026-11-09 07:45:14 +0400
destination:
  file:
    name: CA-E-786-WORKBENCH_FRONTEND-EVAL_CASE--verify-result-grid-context-actions.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-46_FEATURE_WORKBENCH_FRONTEND/06_evaluation
current_scope_unit: WORKBENCH_FRONTEND
claim_target_scope_unit: WORKBENCH_FRONTEND
author: Anatoly Maslennikov
---

## Summary

Verify Workbench read-only result-grid context actions

## Claim scope

The Workbench frontend's read-only result grid and its global filter, sort and grouping interactions.

## Claim

### Prose Claim

A real-browser evaluation **must**:

- open a View containing one query in each standalone and explicit embedded Workbench context, and verify the same read-only grid behavior through their respective backend Workspace/View identities.
- render the complete materialized result through the grid with no cell or row editor. Cell values remain available in full even when the Limited display preference is active.
- expose exactly these context actions: Cell Copy value, Cell Show full value, Row Copy row, Column Sort ascending, Column Sort descending, Group by, Filter and Clear filter. Copy actions preserve the selected value or row; Show full value reveals the complete value; no action mutates the View or result.
- apply sorting and filtering globally across the complete cached result rather than only the currently visible page. Navigate pages after each action and confirm row counts and rows remain globally correct without rerunning the View query.
- group by exactly one selected column in the MVP, with consistent global group counts on every page. No nested grouping, pivoting, export, collaboration or editor action is available.
- keep Adaptive row sizing, Fixed-value visibility and Full/Limited N preferences working while grid actions are used; resize and zoom changes remain display-only and do not rerun the View query.

The evaluation passes only when the grid is read-only, every approved action is available with the stated global behavior, and no unsupported grid feature or query rerun appears.
