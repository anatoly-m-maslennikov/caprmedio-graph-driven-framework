---
identity:
  id: CA-I-8
  ref_id: CA-I-8
context:
  container:
    scope_unit: CA-SU-46
  role: Implementation
  form: Code Synopsis
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Projection
  tier: 3
state:
  status: Active
  version: 1
  updated_at: 2026-11-09 07:55:38 +0400
destination:
  file:
    name: CA-I-8-CODE_SYNOPSIS--workbench-frontend-has-a-sql-completion-defect.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-46_FEATURE_WORKBENCH_FRONTEND/08_implementation
author: Anatoly Maslennikov
---

## Summary

Workbench Frontend has a SQL completion defect

## Claim

### Prose Claim

The inspected Svelte frontend uses shared Workspace transports, CodeMirror and Tabulator. Its custom completion replaces a qualified column’s prefix and inserts status text without escaping apostrophes.

## Details

[SqlEditor.svelte](../../../../../../../LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_WORKBENCH_FRONTEND/src/lib/SqlEditor.svelte) builds quoted-column completion options, then replaces the complete matched token using only the column text. Its status completion appends raw values and a closing quote. These defects contradict Current M468; fix the code, keeping that Method unchanged.

[App.svelte](../../../../../../../LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_WORKBENCH_FRONTEND/src/App.svelte) coordinates View state, Run/Check, result paging, autosave and commands. [ResultsTable.svelte](../../../../../../../LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_WORKBENCH_FRONTEND/src/lib/ResultsTable.svelte) renders the read-only Tabulator grid. [mcp_app_transport.ts](../../../../../../../LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_WORKBENCH_FRONTEND/src/lib/mcp_app_transport.ts) binds the shared App through the native bridge.

TypeScript, workspace tests, standalone build and inline MCP artifact checks passed in the review lane. Browser E2E and fixture-gated native tests were not run. Real native rendering remains deferred. The compact-height target still needs an actual visual comparison. App.svelte is about 350 authored lines, above the split recommendation and below the mandatory 500-line limit; do not split solely for the count.

Refresh direct implementation/evaluator pins only after checking the adopted semantics. Source adoption is not evidence that a new test Version passed.
