---
identity:
  atom_id: CA-P-3040
  ref_id: CA-P-3040@1
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
  - CA-A-1345@1
  - CA-A-1355@1
state:
  version: 1
  status: archived
  updated_at: '2026-11-12T16:36:41.315751+00:00'
destination:
  file:
    name: CA-P-3040@1-TASK--preserve-archive-coverage-and-incremental-indexing.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/099_archived
---
## Summary

Preserve Archive coverage and incremental indexing

## Work

1. Update RMEDO for reread coverage, incremental refresh, and background audit preparation.
2. Review and fix RMEDO against the linked Code Synopses and the Epic decision record.
3. Implement the reviewed RMEDO and verify selected Archives remain queryable, ordinary refresh stays targeted, and performance guards pass. Use the existing Atom ID and Version comments to identify the modules that implement the affected RMEDO and refresh their pins.

## Implementation entry points

- `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_WORKBENCH_BACKEND/service.py`
- `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_WORKBENCH_BACKEND/source_reader.py`
- `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/workbench_tools.py`
