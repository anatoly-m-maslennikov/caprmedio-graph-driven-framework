---
identity:
  atom_id: CA-M-466
  ref_id: CA-M-466
context:
  container:
    scope_unit: CA-SU-46
  role: Method
  form: Solution
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
      <+ Frontend Engineering <+ Libraries and Frameworks
    dependencies:
    - MODEL//CAPRMEDIO <+ Projection
  tier: 4
relations:
  method_for:
  - CA-R-2727
  depends_on:
  - CA-R-3022
  SPECIALIZES:
  - CA-M-222
state:
  status: Active
  version: 9
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-M-466-WORKBENCH_FRONTEND-SOLUTION--use-svelte-typescript-and-vite-for-workbench.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-46_FEATURE_WORKBENCH_FRONTEND/05_method
current_scope_unit: WORKBENCH_FRONTEND
claim_target_scope_unit: WORKBENCH_FRONTEND
author: Anatoly Maslennikov
---
## Summary

Use Svelte, TypeScript and Vite for Workbench

## Claim scope

The Workbench frontend.

## Claim

### Prose Claim

Bind the frontend to the shared backend query, View and saved-resource contract. Preserve supplied request/result/cancellation/stale/error states; the frontend is neither backend authority nor effect owner.

Use Svelte components and TypeScript, built by Vite and served as static assets through the existing Python application. Node is build-only. Keep presentation, formatting, navigation and UI state in the browser; DuckDB owns SQL execution/filtering/sorting/aggregation and stable materialization. Request bounded pages rather than loading a complete large result.

Use complete-result `columns[].has_values` metadata to hide fully empty columns only in non-empty results: NULL, empty string/array/object are empty; false, zero and objects with keys are values. Zero-row results set every column true so headers remain visible. This display rule never changes values/counts and is identical across pages. Reuse a small component palette; add no router, state framework or second web server.
