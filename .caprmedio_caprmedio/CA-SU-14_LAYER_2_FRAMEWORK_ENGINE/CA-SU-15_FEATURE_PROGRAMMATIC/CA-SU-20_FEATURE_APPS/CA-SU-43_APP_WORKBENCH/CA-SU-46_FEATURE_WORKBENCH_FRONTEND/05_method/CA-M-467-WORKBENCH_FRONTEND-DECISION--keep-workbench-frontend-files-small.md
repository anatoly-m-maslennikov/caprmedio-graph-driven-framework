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
    main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Development <+
      Authoring <+ Code Authoring
    dependencies:
    - CAPRMEDIO_MODEL <+ Projection
  tier: 4
relations:
  method_for:
  - CA-R-2727
state:
  status: Active
  version: 4
  updated_at: 2026-11-09 07:45:15 +0400
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

Structure Workbench HTML, CSS, JavaScript, TypeScript and Svelte by responsibility. Splitting a source file above 300 lines is strongly recommended; above 500 lines it is mandatory. Generated build files and dependency lockfiles are not authored source.

Create a small reusable component palette from the start and use it in the page. Split UI components, stateful application behavior and styles where their responsibilities differ; do not create wrappers or arbitrary fragments just to satisfy a line count.

Svelte components provide structured HTML for this frontend. A Python HTML builder is only needed if HTML cannot be structured with the selected frontend tools.
