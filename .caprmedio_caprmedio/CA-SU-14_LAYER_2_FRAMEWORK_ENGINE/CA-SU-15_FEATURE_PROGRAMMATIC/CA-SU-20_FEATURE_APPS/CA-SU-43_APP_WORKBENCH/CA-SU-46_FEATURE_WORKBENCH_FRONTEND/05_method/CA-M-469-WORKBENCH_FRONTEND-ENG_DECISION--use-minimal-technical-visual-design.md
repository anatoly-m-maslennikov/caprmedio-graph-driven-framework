---
atom_id: CA-M-469
current_scope_unit: WORKBENCH_FRONTEND
claim_target_scope_unit: WORKBENCH_FRONTEND
status: Active
author: Anatoly Maslennikov
role: Method
form: Eng Decision
tier: 4
version: 1
subjects:
  active: PROJECT_STRUCTURE <+ Aspect//Visual Design
relations:
  method_for:
  - CA-R-2727
carrier_destination:
  file:
    name: CA-M-469-WORKBENCH_FRONTEND-ENG_DECISION--use-minimal-technical-visual-design.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-46_FEATURE_WORKBENCH_FRONTEND/05_method
updated_at: 2026-11-04 23:19:17 +0400
---

## Summary

Use a minimal technical visual design for Workbench

## Claim scope

Workbench visual presentation.

## Claim

Use a modern, minimal technical interface with light and dark themes. Remember the System theme choice. Use text-only font zoom presets `80`, `90`, `100`, `110`, `125`, `150` and `200` percent for all text, including editor text, headings, tabs, menus, buttons and result/status text; remember the selected preset. Do not scale the whole layout or icons. Use a small reusable component palette with accessible labels, loading state and error state, and a collapsible editor toggle. Do not add a large design system.

Light (Day), Dark (Night) and System are selectable theme modes; remember the selected mode.
