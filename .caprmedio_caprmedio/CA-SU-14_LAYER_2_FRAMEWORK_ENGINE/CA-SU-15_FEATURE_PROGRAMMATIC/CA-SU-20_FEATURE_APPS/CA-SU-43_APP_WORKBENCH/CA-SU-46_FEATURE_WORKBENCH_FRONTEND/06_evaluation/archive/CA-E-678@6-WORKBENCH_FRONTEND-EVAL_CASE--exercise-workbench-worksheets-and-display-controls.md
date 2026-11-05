---
atom_id: CA-E-678
current_scope_unit: WORKBENCH_FRONTEND
claim_target_scope_unit: WORKBENCH_FRONTEND
status: Archived
version: 6
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
    name: CA-E-678@6-WORKBENCH_FRONTEND-EVAL_CASE--exercise-workbench-worksheets-and-display-controls.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-46_FEATURE_WORKBENCH_FRONTEND/06_evaluation/archive
updated_at: 2026-11-05 04:01:26 +0400
---

## Summary

Exercise Workbench worksheets and display controls

## Claim

### Prose Claim

The Workbench interface preserves Worksheet input and uses the shared backend contracts for its query and saved-resource actions. Exercise the accepted controls through the built frontend and real backend. Prefer complete browser flows over checks of component internals. Keep focused tests only for behavior not covered end-to-end.

## Details

| Fixture | Expected outcome |
| --- | --- |
| Light, Dark and System | Each mode is selectable; the choice is remembered; focus and result text remain readable. |
| Compact navigation | The top header shows Workbench and the selected Project name. `Settings` and `Saved Queries and Worksheets` are at its right, on the same level as Workbench; current Worksheet tabs are below. Theme and Zoom work while the Settings panel is hidden. |
| Text zoom | Editor, buttons, tabs, menus, headings, result and status text change size. Layout dimensions and icons are not multiplied. |
| Two Worksheets | Inputs and displayed results stay with their own tabs. Closing unsaved input asks first. |
| Five-second autosave and reload | Whole scripts, current Worksheet names and open-tab state restore without clicking Save. Browser unload flushing is best effort; storage failures are visible and are not false success. |
| Current Worksheet name | The Operator can rename a current Worksheet; five-second browser autosave and reload retain that name. Save Worksheet copies the optional name into a new entry without renaming an existing saved item. |
| Native window close warning | Unsaved input uses the browser warning when the browser permits it; no cross-browser controller is added. |
| Hide editor | One `Hide editor` control hides and reopens the same input while preserving its script and cursor in the current page. |
| Open Saved modal | `Cmd+P` → `Open Saved` opens a modal; no separate toolbar button or dedicated shortcut is present. The modal has an autofocus ID/URL input. Native `Cmd+V` paste is accepted; Enter opens without execution; Escape and Cancel close it; no inline open form is shown. |
| Completion | Actual tables and columns are offered, including quoted dotted/spaced content columns. A prefix such as `status = 'Act` offers and inserts `Active` with correct quoting. The editor does not execute SQL or create a saved record for suggestions. |
| Hotkey hints | Each known shortcut appears inside its action button or immediately beside it, including Run and Check. |
| Explicit saves | Run, Check, pagination and query errors create no saved Journal entries and do not mark local edits saved. Explicit Save and Save Worksheet create entries. Browser draft autosave continues. |
| Query editor heading | The title is `Query editor`. A saved ID link is at the right of that same heading row, not below the editor. |
| Cursor actions | Run and Cmd+Enter execute the current statement; Check and Shift+Cmd+Enter check it; Save saves it; Save Worksheet saves the entire script. |
| Saved resource links | Show ID, optional creation name and full URL, open an ID or URL without execution, and show recent queries and Worksheets in one tab. App-owned links reuse the current Workbench browser context; saved items are not renamed. |
| Save during a multi-statement Worksheet | Preserve the complete local draft; saving only one statement does not falsely mark the whole Worksheet saved. |
| Existing error and pagination controls | Errors remain visible, busy requests cannot duplicate from shortcuts/buttons, and paged columns/values stay complete. |

| Command palette | Cmd+P opens from the editor and other Workbench controls with search focused. Search covers every current user action; Arrow Up/Ctrl+P and Arrow Down/Ctrl+N move selection, Enter invokes the same available action as its control, and Escape closes. Settings, focus changes, Worksheet switching and query actions work without a mouse. |
| Current settings | Theme, Zoom and workspace preferences restore from local storage on reload. |

Browser end-to-end checks cover SQL editing and execution with visible results; current Worksheet rename, autosave/reload, Save Worksheet and Open Saved without execution; and command-palette keyboard navigation, including Ctrl+P and Ctrl+N. Assertions use visible controls and outputs, not private Svelte or CodeMirror state.

Result headers show the column name separately from the SQL type on the line below. SQL names, types and result values remain unchanged.
