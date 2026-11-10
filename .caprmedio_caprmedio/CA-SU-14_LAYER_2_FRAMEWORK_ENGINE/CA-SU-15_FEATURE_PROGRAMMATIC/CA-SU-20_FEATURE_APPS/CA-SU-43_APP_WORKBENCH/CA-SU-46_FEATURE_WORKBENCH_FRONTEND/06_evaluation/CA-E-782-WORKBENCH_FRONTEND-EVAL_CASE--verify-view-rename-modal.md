---
identity:
  atom_id: CA-E-782
  ref_id: CA-E-782
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
  version: 4
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-E-782-WORKBENCH_FRONTEND-EVAL_CASE--verify-view-rename-modal.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-46_FEATURE_WORKBENCH_FRONTEND/06_evaluation
current_scope_unit: WORKBENCH_FRONTEND
claim_target_scope_unit: WORKBENCH_FRONTEND
author: Anatoly Maslennikov
---
## Summary

Verify the shared View rename modal

## Claim

### Prose Claim

Use the built Workbench and real Workspace backend. Double-click current View name or choose Rename View from palette: the same shared modal opens with current displayed name prefilled. Confirm updates current View and existing persistence/local state through refresh/reload; Cancel/Escape leaves name unchanged. Single click and unrelated query/autosave controls introduce neither click-only rename nor separate workflow. Prefer visible browser E2E and existing rename API, not private Svelte state.
