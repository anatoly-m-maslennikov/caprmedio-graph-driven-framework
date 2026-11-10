---
identity:
  atom_id: CA-M-469
  ref_id: CA-M-469
context:
  container:
    scope_unit: CA-SU-46
  role: Method
  form: Decision
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspect//Visual Design
  tier: 4
relations:
  method_for:
  - CA-R-2727
state:
  status: Active
  version: 11
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-M-469-WORKBENCH_FRONTEND-DECISION--use-a-minimal-technical-visual-design-for-workbench.md
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

Use a compact, modern, minimal technical interface with selectable remembered Light/Dark/System theme and available window width, not a fixed centered workspace. Reduce repeated headings, chrome and empty space while controls remain readable, accessible and usable at selected zoom. Top header shows Workbench/Project; Settings and combined Bookmarks/Saved Tabs are top-right, with Tab tabs below and hotkey hints in/next to actions.

Settings starts hidden and orders Theme, Interface text zoom, Content text zoom, Interface zoom, Density. Defaults are System and three 100% zooms; Comfortable density except explicit `embedded=1`, where Compact is default. Only plugin opener adds `embedded=1`; screen size/Workspace does not infer it and saved browser preference wins. Interface/Content text zoom independently use 80/90/100/110/125/150/200% and persist; Interface text affects chrome/headers, Content text affects query/cells/full values. Whole-interface zoom and Density persist independently; text zoom changes neither layout nor icon scale. Upgrade old single text zoom into both values.

Title input `Query editor`, with saved link on its header row. That complete header is the sole keyboard-accessible Hide/Show editor control; no toolbar toggle. Open Saved is command-palette-only native dialog with autofocus, native paste, Enter-open-without-execution and Escape/Cancel. Keep saved library combined but distinguish Bookmark/Tab kinds (historical `kind: view` remains a compatibility identifier). Use the shared accessible component palette and native Cmd+P command palette for existing actions/shortcuts (Settings, focus, Tabs, query, saved/open, editor, pages/grid, theme/zooms/density), keyboard navigation and the same handlers/availability—no framework, backend, extra action or design system.

Show result column name then smaller muted SQL type; preserve readable dark-grid states and render every source newline in cells/full values with pre-wrap. CA-M-492 owns read-only grid/action/group/cache detail. At 100%, target half the prior 80%-layout height without a breakpoint framework. Provide Format beside Query editor and in palette via the canonical formatter only.
