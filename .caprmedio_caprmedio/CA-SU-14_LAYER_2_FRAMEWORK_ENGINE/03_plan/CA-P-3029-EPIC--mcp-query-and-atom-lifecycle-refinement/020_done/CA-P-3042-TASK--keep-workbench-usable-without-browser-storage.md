---
identity:
  atom_id: CA-P-3042
  ref_id: CA-P-3042
context:
  role: plan
  form: Plan
  label: Task
  container:
    atom: CA-P-3029
  tier: 3
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
relations:
  DERIVED_FROM:
  - CA-A-1349@1
  - CA-A-1358@1
state:
  version: 1
  status: done
  updated_at: '2026-11-12T16:36:42.267477+00:00'
destination:
  file:
    name: CA-P-3042-TASK--keep-workbench-usable-without-browser-storage.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-3029-EPIC--mcp-query-and-atom-lifecycle-refinement/020_done
---
## Summary

Keep Workbench usable without browser storage

## Work

1. Update RMEDO for Workspace binding, embedded density, and storage failure.
2. Review and fix RMEDO against the linked Code Synopses and the Epic decision record.
3. Implement the reviewed RMEDO and verify stable Workspace identity, canonical Project name, and a warning with in-memory edits. Use the existing Atom ID and Version comments to identify the modules that implement the affected RMEDO and refresh their pins.

## Implementation entry points

- `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_WORKBENCH_FRONTEND/src/App.svelte`
- `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/workbench_tools.py`
- `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_WORKBENCH_FRONTEND/src/lib/workspace.js`
