---
identity:
  atom_id: CA-M-467
  ref_id: CA-M-467
context:
  container:
    scope_unit: CA-SU-46
  role: Method
  form: Decision
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
      <+ Frontend Engineering <+ Code Style
    dependencies:
    - MODEL//CAPRMEDIO <+ Projection
  tier: 4
relations:
  method_for:
  - CA-R-2727
  depends_on:
  - CA-R-3022
state:
  status: Active
  version: 5
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-M-467-WORKBENCH_FRONTEND-DECISION--keep-workbench-frontend-files-small.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-46_FEATURE_WORKBENCH_FRONTEND/05_method
current_scope_unit: WORKBENCH_FRONTEND
claim_target_scope_unit: WORKBENCH_FRONTEND
author: Anatoly Maslennikov
---
## Summary

Keep Workbench frontend files small

## Claim scope

The Workbench frontend.

## Claim

### Prose Claim

Structure authored HTML, CSS, JavaScript, TypeScript and Svelte by responsibility. Split above 300 lines is strongly recommended and above 500 mandatory; generated build files, lockfiles, vendored sources and frozen history are excluded. Start with a small reusable component palette, separating components, stateful behavior and styles when responsibilities differ, without arbitrary wrappers/fragments for line count. Use Svelte for structured HTML; use a Python HTML builder only when selected frontend tools cannot structure it.
