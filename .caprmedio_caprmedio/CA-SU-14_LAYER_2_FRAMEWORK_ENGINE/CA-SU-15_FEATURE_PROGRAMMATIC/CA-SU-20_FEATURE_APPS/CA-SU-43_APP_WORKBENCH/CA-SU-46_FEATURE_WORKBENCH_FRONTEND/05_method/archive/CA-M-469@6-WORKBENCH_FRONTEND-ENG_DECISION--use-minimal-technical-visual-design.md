---
atom_id: CA-M-469
ref_id: CA-M-469@6
container:
  scope_unit: CA-SU-46
role: Method
form: Eng Decision
topics:
  main_subject: PROJECT_STRUCTURE <+ Aspect//Visual Design
tier: 4
relations:
  method_for:
  - CA-R-2727
status: Archived
version: 6
updated_at: 2026-11-05 19:04:52 +0400
carrier_destination:
  file:
    name: CA-M-469-WORKBENCH_FRONTEND-ENG_DECISION--use-a-minimal-technical-visual-design-for-workbench.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-46_FEATURE_WORKBENCH_FRONTEND/05_method/archive
current_scope_unit: WORKBENCH_FRONTEND
claim_target_scope_unit: WORKBENCH_FRONTEND
author: Anatoly Maslennikov
---
## Summary

Use a minimal technical visual design for Workbench

## Claim scope

Workbench visual presentation.

## Claim

### Prose Claim

Use a compact, modern, minimal technical interface with selectable Light (Day), Dark (Night) and System themes, remembering the selected mode. Reduce repeated headings, header height, logo/button padding and unnecessary vertical space while keeping controls readable, accessible and available at the selected zoom. Show Workbench and the selected Project name in the top header; put Settings and Saved Queries and Views at the top right on the same level, with current View tabs below. Show each available hotkey inside its action button or immediately beside it.

Keep the Settings panel hidden initially and arrange its controls vertically as Theme, Text zoom, Interface zoom and Density. Defaults are Theme System, Text zoom 100%, Interface zoom 100%, and Compact density only for an explicit `embedded=1` URL; ordinary standalone URLs default to Comfortable. Saved explicit browser preferences win. The plugin opener alone adds `embedded=1`; do not infer embedding from screen size or Workspace presence.

Use text-only font zoom presets `80`, `90`, `100`, `110`, `125`, `150` and `200` percent for editor text, headings, tabs, menus, buttons and result/status text; remember the selected preset and restrict it to text. Use the same fixed presets for independent Interface zoom of the whole interface, remember it in browser local storage, and keep it independent from text zoom and Density. Do not add a large design system or separate settings registry.

Title the input area `Query editor`; place its `Saved: <ID>` link on the same header row at the right. Use one `Hide editor` control for the active View. Offer `Open Saved` only in the command palette and use a native dialog with autofocus, native `Cmd+V` paste, Enter to open without executing SQL, and Escape or Cancel to close. Keep the Saved Queries and Views library combined and status-value completion text-only and unobtrusive.

Use a small reusable component palette with accessible labels, loading state and error state. Do not add a large design system. Use a native dialog for a searchable, keyboard-operated command palette on Cmd+P. List existing UI actions and their available shortcuts, including Theme, Text zoom, Interface zoom, Density and View rename, and invoke the same handlers as their controls. Support Arrow Up/Ctrl+P, Arrow Down/Ctrl+N, Enter and Escape. Keep Theme, Text zoom, Interface zoom, Density and workspace preferences in local storage. Do not add a command-palette framework or another backend. Keep result column names and SQL types visually separate: name first, type below in smaller muted text.
