---
atom_id: CA-M-469
current_scope_unit: WORKBENCH_FRONTEND
claim_target_scope_unit: WORKBENCH_FRONTEND
status: Archived
author: Anatoly Maslennikov
role: Method
form: Eng Decision
tier: 4
version: 5
subjects:
  active: PROJECT_STRUCTURE <+ Aspect//Visual Design
relations:
  method_for:
  - CA-R-2727
carrier_destination:
  file:
    name: CA-M-469@5-WORKBENCH_FRONTEND-ENG_DECISION--use-minimal-technical-visual-design.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-46_FEATURE_WORKBENCH_FRONTEND/05_method/archive
updated_at: 2026-11-05 04:01:26 +0400
---

## Summary

Use a minimal technical visual design for Workbench

## Claim scope

Workbench visual presentation.

## Claim

Use a compact, modern, minimal technical interface with light and dark themes. Reduce repeated headings, large paddings and unnecessary vertical space while keeping controls readable and Zoom available. Show Workbench and the selected Project name in the top header. Put `Settings` and `Saved Queries and Worksheets` at the top-right of that header, on the same level as Workbench. Keep current Worksheet tabs in the workspace below. Show each available hotkey inside its action button or immediately beside it. Keep the Settings panel hidden initially; apply Theme and text `Zoom` preferences on page load even while it is hidden. Title the input area `Query editor`; place its `Saved: <ID>` link on the same header row at the right. Use one `Hide editor` control for the active Worksheet. Remember the System theme choice. Use text-only font zoom presets `80`, `90`, `100`, `110`, `125`, `150` and `200` percent for all text, including editor text, headings, tabs, menus, buttons and result/status text; remember the selected preset. Do not scale the whole layout or icons. Use a small reusable component palette with accessible labels, loading state and error state. Do not add a large design system.

Offer `Open Saved` only in the command palette, without a separate toolbar button or dedicated shortcut. It opens a modal with an autofocus ID/URL input; allow native `Cmd+V` paste, Enter to open without executing SQL, and Escape or Cancel to close. Keep the Saved Queries and Worksheets view as the combined library, and keep status-value completion text-only and unobtrusive.

Light (Day), Dark (Night) and System are selectable theme modes; remember the selected mode.

Use a native dialog for a searchable, keyboard-operated command palette on Cmd+P. List existing UI actions and their available shortcuts, and invoke the same handlers as their controls. Support Arrow Up/Ctrl+P, Arrow Down/Ctrl+N, Enter and Escape. Keep Theme, Zoom and workspace preferences in local storage. Do not add a command-palette framework or another backend.

Keep result column names and SQL types visually separate: name first, type below in smaller muted text.
