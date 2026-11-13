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
    main_subject: MODEL//CAPRMEDIO <+ Projection
  tier: 5
relations:
  evaluation_for:
  - CA-M-492
  - CA-D-674
state:
  status: active
  version: 6
  updated_at: '2026-11-12T16:57:58.468211+00:00'
destination:
  file:
    name: CA-E-786-WORKBENCH_FRONTEND-EVAL_CASE--verify-workbench-read-only-result-grid-context-actions.md
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

In standalone and explicit embedded context, open a Tab containing one complete read-only SQL query and verify equivalent read-only grid behavior through each Workspace/View identity. Complete materialized values remain available even under Limited display. Expose exactly Cell Copy value, Cell Show full value, Row Copy row, Column Sort ascending/descending, Group by, Filter and Clear filter; copy/show preserve full selected data and none mutates View/result.

Sort/filter operate globally over complete cache and pages remain correct without rerunning SQL. Group exactly one selected column with global counts; no nested group, pivot, export, collaboration or editor action appears in this menu (shared file delivery remains outside it). Adaptive/Fixed/Full/Limited, resize and zoom stay display-only. Pass only when every approved action has this behavior and no unsupported feature/replay appears.
