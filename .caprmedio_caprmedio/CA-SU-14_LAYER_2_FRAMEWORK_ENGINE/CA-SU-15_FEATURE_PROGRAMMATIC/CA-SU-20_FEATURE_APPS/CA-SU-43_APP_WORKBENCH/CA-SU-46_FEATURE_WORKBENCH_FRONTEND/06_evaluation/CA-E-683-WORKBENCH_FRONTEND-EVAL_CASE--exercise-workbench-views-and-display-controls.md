---
atom_id: CA-E-683
ref_id: CA-E-683
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
  - CA-R-2776
  - CA-M-468
  - CA-M-469
  - CA-M-470
  - CA-D-674
status: Active
version: 2
updated_at: 2026-11-05 16:45:35 +0400
carrier_destination:
  file:
    name: CA-E-683-WORKBENCH_FRONTEND-EVAL_CASE--exercise-workbench-views-and-display-controls.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-46_FEATURE_WORKBENCH_FRONTEND/06_evaluation
current_scope_unit: WORKBENCH_FRONTEND
claim_target_scope_unit: WORKBENCH_FRONTEND
author: Anatoly Maslennikov
---

## Summary

Exercise Workbench Views and display controls

## Claim

### Prose Claim

The Workbench interface preserves View input and uses the shared backend contracts for its query and saved-resource actions. Exercise the accepted controls through the built frontend and real backend. Prefer complete browser flows over checks of component internals. Keep focused tests only for behavior not covered end-to-end.

## Details

| Fixture | Expected outcome |
| --- | --- |
| Light, Dark and System | Each mode is selectable; the choice is remembered; focus and result text remain readable. |
| Compact and Comfortable density | Compact is the default and fits a representative laptop viewport; Comfortable is selectable for a representative desktop viewport. The test verifies the selected density, not physical screen-size detection. |
| Compact navigation | The top header shows Workbench and the selected Project name. Settings and Saved Queries and Views are at the top of the window, on the right at the same level as Workbench; current View tabs are below. Theme, Zoom and density work while the Settings panel is hidden. |
| Text zoom | Editor, buttons, tabs, menus, headings, result and status text change size. Layout dimensions and icons are not multiplied. |
| Two Views | Inputs and displayed results stay with their own tabs. Closing unsaved input asks first. |
| Five-second autosave and reload | Whole scripts, current View names, divider/density settings and open-tab state restore without clicking Save. Browser unload flushing is best effort; storage failures are visible and are not false success. |
| Current View name | The Operator can rename a current View; five-second browser autosave and reload retain that name. Save View copies the optional name into a new entry without renaming an existing saved item. |
| Native window close warning | Unsaved input uses the browser warning when the browser permits it; no cross-browser controller is added. |
| Hide editor | One Hide editor control hides and reopens the same input while preserving its script and cursor in the current page. |
| Open Saved modal | Cmd+P -> Open Saved opens a modal; no separate toolbar button or dedicated shortcut is present. The modal has an autofocus ID/URL input. Native Cmd+V paste is accepted; Enter opens without execution; Escape and Cancel close it; no inline open form is shown. |
| Completion | Actual tables and columns are offered, including quoted dotted/spaced content columns. A prefix such as status = 'Act offers and inserts Active with correct quoting. The editor does not execute SQL or create a saved record for suggestions. |
| Hotkey hints | Each known shortcut appears inside its action button or immediately beside it, including Run and Check. |
| Default query actions | Run, Check, pagination and query errors create no saved Journal entries and do not mark local edits saved. Cmd+Enter runs and Shift+Cmd+Enter checks the current statement. |
| Run & Save | Run & Save executes the current statement, then creates a saved query only after a successful Run. The answer shows its ID, kind and full URL only when save succeeds. A failed save leaves the visible result rows, query ID, previous saved identity and dirty state, and shows the save error. |
| Query editor heading | The title is Query editor. A saved ID link is at the right of that same heading row, not below the editor. |
| Cursor actions | Run and Cmd+Enter execute the current statement; Check and Shift+Cmd+Enter check it; Run & Save saves the current statement only after its Run succeeds; Save View saves the entire script. |
| Saved resource links | Show ID, optional creation name and full URL, open an ID or URL without execution, and show recent queries and Views in one tab. App-owned links reuse the current Workbench browser context; saved items are not renamed. Existing historical worksheet entries remain loadable. |
| Save during a multi-statement View | Preserve the complete local draft; Run & Save saves only the current statement; Save View saves the whole script. A current View is not falsely marked saved after a failed query or save. |
| Existing error and pagination controls | Errors remain visible, busy requests cannot duplicate from shortcuts/buttons, and paged columns/values stay complete. |
| Command palette | Cmd+P opens from the editor and other Workbench controls with search focused. Search covers every current user action; Arrow Up/Ctrl+P and Arrow Down/Ctrl+N move selection, Enter invokes the same available action as its control, and Escape closes. Settings, focus changes, View switching and query actions work without a mouse. |
| Current settings | Theme, Zoom, density and workspace preferences restore from local storage on reload. |

Browser end-to-end checks cover SQL editing and execution with visible results; current View rename, autosave/reload, Run & Save, Save View and Open Saved without execution; layout density; and command-palette keyboard navigation, including Ctrl+P and Ctrl+N. Assertions use visible controls and outputs, not private Svelte or CodeMirror state.

Result headers show the column name separately from the SQL type on the line below. SQL names, types and result values remain unchanged.

Verify the UI accepts the completed partial Run response, retains its rows/query ID, and displays save_error without replacing the prior saved identity or marking the View clean.
