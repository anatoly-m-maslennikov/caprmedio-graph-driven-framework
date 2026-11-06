---
atom_id: CA-M-469
ref_id: CA-M-469
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
status: Active
version: 7
updated_at: 2026-11-06 20:37:19 +0400
carrier_destination:
  file:
    name: CA-M-469-WORKBENCH_FRONTEND-ENG_DECISION--use-a-minimal-technical-visual-design-for-workbench.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-46_FEATURE_WORKBENCH_FRONTEND/05_method
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

Use a compact, modern, minimal technical interface with selectable Light (Day), Dark (Night) and System themes, remembering the selected mode. Use the available window width rather than a centered fixed-width workspace. Reduce repeated headings, header height, logo/button padding and unnecessary vertical space while keeping controls readable, accessible and available at the selected zoom. Show Workbench and the selected Project name in the top header; put Settings and Saved Queries and Views at the top right on the same level, with current View tabs below. Show each available hotkey inside its action button or immediately beside it.

Keep the Settings panel hidden initially and arrange its controls vertically as Theme, Interface text zoom, Content text zoom, Interface zoom and Density. Defaults are Theme System, Interface text zoom 100%, Content text zoom 100% and Interface zoom 100%; Compact density is the default only for an explicit `embedded=1` URL, while an ordinary standalone URL defaults to Comfortable. Saved explicit browser preferences win. The plugin opener alone adds `embedded=1`; do not infer embedding from screen size or Workspace presence. Settings labels and values may use larger text for readability without changing the compact control spacing.

Provide independent text-only Interface and Content zoom presets `80`, `90`, `100`, `110`, `125`, `150` and `200` percent. Interface text zoom scales titles, tabs, menus, buttons, labels, Settings and column headers/types; Content text zoom scales query text, result cells and full-value text. Remember both settings separately in browser local storage. Use the same fixed presets for independent whole-Interface zoom, remember it locally, and keep it independent from both text zooms and Density. Neither text zoom changes layout or icon scale. When upgrading an old single text-zoom preference, use its value as the initial value of both independent text zooms.

Title the input area `Query editor`; place its `Saved: <ID>` link on the same header row at the right. Use the full Query editor header panel as the only collapse control for the active View, with pale `Hide editor` or `Show editor` text on the right. Keep it keyboard-accessible and do not add a separate toolbar toggle. Offer `Open Saved` only in the command palette and use a native dialog with autofocus, native `Cmd+V` paste, Enter to open without executing SQL, and Escape or Cancel to close. Keep the Saved Queries and Views library combined and status-value completion text-only and unobtrusive.

Use a small reusable component palette with accessible labels, loading state and error state. Do not add a large design system. Use a native dialog for a searchable, keyboard-operated command palette on Cmd+P. List existing UI actions and their available shortcuts, including Theme, Interface text zoom, Content text zoom, Interface zoom, Density and View rename, and invoke the same handlers as their controls. Support Arrow Up/Ctrl+P, Arrow Down/Ctrl+N, Enter and Escape. Keep Theme, both text zooms, Interface zoom, Density and workspace preferences in local storage. Do not add a command-palette framework, another backend or extra menu actions.

Keep result column names and SQL types visually separate: show the name first and the type below in smaller, pale/muted text in both light and dark themes. The dark Tabulator grid must keep headers, cells, borders and hover/focus/selected states readable. Display source newlines in Content cells and full-value views with pre-wrap presentation; do not collapse a single newline into a space or require a blank line.
