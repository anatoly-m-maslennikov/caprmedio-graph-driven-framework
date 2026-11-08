---
identity:
  atom_id: CA-E-683
  ref_id: CA-E-683@6-draft
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
  - CA-R-2776
  - CA-M-468
  - CA-M-469
  - CA-M-470
  - CA-D-674
state:
  status: Draft
  version: 6
  updated_at: 2026-11-08 20:06:18 +0400
destination:
  file:
    name: CA-E-683@6-draft-WORKBENCH_FRONTEND-EVAL_CASE--exercise-workbench-views-and-display-controls.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-46_FEATURE_WORKBENCH_FRONTEND/06_evaluation/draft/p2715
current_scope_unit: WORKBENCH_FRONTEND
claim_target_scope_unit: WORKBENCH_FRONTEND
author: Anatoly Maslennikov
---

## Summary

Exercise Workbench Views and display controls

## Claim

### Prose Claim

The Workbench interface preserves View input and uses the shared backend contracts for its query and saved-resource actions. Exercise the accepted controls through the built frontend and real backend. Prefer complete browser flows over checks of component internals. Keep focused tests only for behavior not covered end-to-end.

Verify Format through its button and command-palette entry in the shared standalone/native Query editor. A compact query becomes the Method's line layout, including leading commas, uppercase SELECT, lowercase clauses, two-space indentation and a separate semicolon. Quoted identifiers, string values, comments, CTEs and nested queries keep their meaning. Formatting twice is stable. The editor reports an ordinary unsaved edit, existing autosave/restore retains it, and no Run, Check or Save is sent. If the library rejects input, display the error and keep the original query and existing results unchanged.

Exercise the View actions through the built frontend and real backend. Clicking a View's Saved link preserves the View count, active View ID, unsaved edits and existing results. Opening the same saved ID or URL through Open Saved focuses the matching open View rather than creating another; different saved IDs with equal SQL are not merged. Verify standalone reload retains the saved identity needed for this reuse.

Rename a non-active tab through its context menu and rename the current View through the palette; the dialog starts with its current display name. Duplicate through both entry points. Verify new stable IDs, exact query and cursor copies, names such as `Report(1)` and `Report(2)`, collision handling, focus and persistence. The source stays unchanged; copies have no prior result or saved-item identity, and no Run, Check or Save is sent. Running a copy later produces its own result without changing the source. Check the same duplicate operation through the native bridge.

## Details

| Fixture | Expected outcome |
| --- | --- |
| Light, Dark and System | Each mode is selectable; the choice is remembered; focus, result text and the dark Tabulator grid remain readable. |
| Compact and Comfortable density | Compact is the default only for an explicit `embedded=1` URL; an ordinary standalone URL defaults to Comfortable. The test verifies the selected density, not physical screen-size detection. |
| Compact navigation | The top header shows Workbench and the selected Project name. Settings and Saved Queries and Views are at the top of the window, on the right at the same level as Workbench; current View tabs are below. Theme, Interface text zoom, Content text zoom, whole-Interface zoom and Density work while the Settings panel is hidden. Settings text remains readable even with compact spacing. |
| Text zoom | Interface text zoom changes titles, tabs, menus, buttons, labels, Settings and column headers/types; Content text zoom changes query text, result cells and full-value text. Both persist independently. Whole-Interface zoom, Density and icon/layout scale remain separate. |
| Two Views | Inputs and displayed results stay with their own tabs. Closing unsaved input asks first. |
| Five-second autosave and reload | Whole queries, current View names, divider/density settings, both text zooms, whole-Interface zoom and open-tab state restore without clicking Save. Browser unload flushing is best effort; storage failures are visible and are not false success. |
| Current View name | The Operator can rename a current View; five-second browser autosave and reload retain that name. Save View copies the optional name into a new entry without renaming an existing saved item. |
| Native window close warning | Unsaved input uses the browser warning when the browser permits it; no cross-browser controller is added. |
| Hide editor | The full Query editor header panel is the only collapse control. Pale Hide editor or Show editor text appears on its right, and the same View preserves its query and cursor when reopened; no separate toolbar toggle is present. |
| Open Saved modal | Cmd+P -> Open Saved opens a modal; no separate toolbar button or dedicated shortcut is present. The modal has an autofocus ID/URL input. Native Cmd+V paste is accepted; Enter opens without execution; Escape and Cancel close it; no inline open form is shown. |
| Completion | Actual tables and columns are offered, including dotted Content paths with snake_case segments such as `content.claim.prose_claim`; space-based Content names are not required. A prefix on the actual Header Status column such as `header_status = 'Act` offers and inserts `Active` with correct quoting. The editor does not execute SQL or create a saved record for suggestions. |
| Hotkey hints | Each known shortcut appears inside its action button or immediately beside it, including Run and Check. |
| Default query actions | Run, Check, pagination and query errors create no saved Journal entries and do not mark local edits saved. Cmd+Enter runs and Shift+Cmd+Enter checks the whole current View query. |
| Run & Save | Run & Save executes the whole current View query, then creates a saved query only after a successful Run. The answer shows its ID, kind and full URL only when save succeeds. A failed save leaves the visible result rows, query ID, previous saved identity and dirty state, and shows the save error. |
| Query editor heading | The title is Query editor. A saved ID link is at the right of that same heading row, not below the editor. |
| View actions | Run and Cmd+Enter execute the whole current View query; Check and Shift+Cmd+Enter check it; Run & Save saves it only after its Run succeeds; Save View saves the entire View query text. Multiple SQL statements are rejected rather than split by cursor. |
| Saved resource links | Show ID, optional creation name and full URL, open an ID or URL without execution, and show recent queries and Views in one tab. App-owned links reuse the current Workbench browser context; saved items are not renamed. Existing historical worksheet entries remain loadable. |
| Save during a View | Preserve the complete local draft; Run & Save saves the current View query only after success; Save View saves the whole View query. A current View is not falsely marked saved after a failed query or save. |
| Existing error and pagination controls | Errors remain visible, busy requests cannot duplicate from shortcuts/buttons, and paged columns/values stay complete. Content cells and full-value views show every source newline with pre-wrap presentation. |
| Command palette | Cmd+P opens from the editor and other Workbench controls with search focused. Search covers every current user action; Arrow Up/Ctrl+P and Arrow Down/Ctrl+N move selection, Enter invokes the same available action as its control, and Escape closes. Settings, focus changes, View switching and query actions work without a mouse. |
| Current settings | Theme, Interface text zoom, Content text zoom, whole-Interface zoom, Density and workspace preferences restore from local storage on reload. |

Browser end-to-end checks cover SQL editing and execution with visible results; current View rename, autosave/reload, Run & Save, Save View and Open Saved without execution; layout density; and command-palette keyboard navigation, including Ctrl+P and Ctrl+N. Assertions use visible controls and outputs, not private Svelte or CodeMirror state.

Result headers show the column name separately from the SQL type on the line below in smaller, pale/muted text in both themes. SQL names, types and result values remain unchanged.

Verify the UI accepts the completed partial Run response, retains its rows/query ID, and displays save_error without replacing the prior saved identity or marking the View clean.
