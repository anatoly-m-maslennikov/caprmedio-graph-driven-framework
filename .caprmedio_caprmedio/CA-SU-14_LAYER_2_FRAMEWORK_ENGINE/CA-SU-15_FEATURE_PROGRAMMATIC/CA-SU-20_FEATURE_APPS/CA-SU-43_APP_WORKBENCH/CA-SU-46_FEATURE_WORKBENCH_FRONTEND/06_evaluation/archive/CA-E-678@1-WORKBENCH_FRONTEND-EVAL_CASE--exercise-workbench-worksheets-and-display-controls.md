---
atom_id: CA-E-678
current_scope_unit: WORKBENCH_FRONTEND
claim_target_scope_unit: WORKBENCH_FRONTEND
status: Archived
version: 1
author: Anatoly Maslennikov
role: Evaluation
form: Eval Case
tier: 5
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations:
  evaluation_for:
  - CA-R-2727
  - CA-R-2776
  - CA-M-468
  - CA-M-469
  - CA-M-470
  - CA-D-674
carrier_destination:
  file:
    name: CA-E-678@1-WORKBENCH_FRONTEND-EVAL_CASE--exercise-workbench-worksheets-and-display-controls.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-46_FEATURE_WORKBENCH_FRONTEND/06_evaluation/archive
updated_at: 2026-11-04 23:19:17 +0400
---

## Summary

Exercise Workbench worksheets and display controls

## Claim

### Prose Claim

The Workbench interface preserves Worksheet input and uses the shared backend contracts for its query and saved-resource actions. Exercise the accepted controls through the built frontend and focused component or state checks.

## Details

| Fixture | Expected outcome |
| --- | --- |
| Light, Dark and System | Each mode is selectable; the choice is remembered; focus and result text remain readable. |
| Text zoom | Editor, buttons, tabs, menus, headings, result and status text change size. Layout dimensions and icons are not multiplied. |
| Two Worksheets | Inputs and displayed results stay with their own tabs. Closing unsaved input asks first. |
| Five-second autosave and reload | Whole scripts and open-tab state restore without clicking Save. Browser unload flushing is best effort; storage failures are visible and are not false success. |
| Native window close warning | Unsaved input uses the browser warning when the browser permits it; no cross-browser controller is added. |
| Collapsed editor | The spoiler expands the same input and preserves its cursor while the page remains open. |
| Completion | Actual tables and columns are offered, including quoted dotted/spaced content columns; the editor does not execute SQL for suggestions. |
| Cursor actions | Run and Cmd+Enter execute the current statement; Check and Shift+Cmd+Enter check it; Save saves it; Save Worksheet saves the entire script. |
| Saved resource links | Show ID and full URL, open an ID or URL without execution, and show recent queries and Worksheets. App-owned links reuse the current Workbench browser context. |
| Save during a multi-statement Worksheet | Preserve the complete local draft; saving only one statement does not falsely mark the whole Worksheet saved. |
| Existing error and pagination controls | Errors remain visible, busy requests cannot duplicate from shortcuts/buttons, and paged columns/values stay complete. |
