---
atom_id: CA-E-782
ref_id: CA-E-782
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
status: Active
version: 1
updated_at: 2026-11-05 19:04:52 +0400
carrier_destination:
  file:
    name: CA-E-782-WORKBENCH_FRONTEND-EVAL_CASE--verify-the-shared-view-rename-modal.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-46_FEATURE_WORKBENCH_FRONTEND/06_evaluation
current_scope_unit: WORKBENCH_FRONTEND
claim_target_scope_unit: WORKBENCH_FRONTEND
author: Anatoly Maslennikov
---
## Summary

Verify the shared View rename modal

## Claim

### Prose Claim

Exercise the built Workbench with the real Workspace backend. A double-click on the current View name opens the existing shared rename modal with the currently displayed name prefilled; the Operator can edit and confirm the name through the existing rename contract.

| Case | Expected result |
| --- | --- |
| Double-click the current View name | The shared rename modal opens with that View's current name, not an empty value. |
| Edit the prefilled name and confirm | The current View shows the new name and the existing Workspace persistence/local browser state retain it after refresh or reload. |
| Cancel or press Escape | The modal closes and the View name remains unchanged. |
| Open Rename View from the command palette | The same shared prefilled modal and confirm/cancel behavior are used. |
| Click the View name once or use unrelated query/autosave controls | No new click-only rename button or separate rename workflow is introduced. |

Prefer browser end-to-end checks with visible controls and the existing rename API; do not inspect private Svelte state.
