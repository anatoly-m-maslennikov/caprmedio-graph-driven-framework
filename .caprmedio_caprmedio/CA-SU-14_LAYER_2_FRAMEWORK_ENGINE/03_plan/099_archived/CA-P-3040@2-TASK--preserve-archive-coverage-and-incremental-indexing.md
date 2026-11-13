---
identity:
  atom_id: CA-P-3040
  ref_id: CA-P-3040@2
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
  version: 2
  status: archived
  updated_at: '2026-11-13T09:53:50.375245+00:00'
destination:
  file:
    name: CA-P-3040@2-TASK--preserve-archive-coverage-and-incremental-indexing.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/099_archived
---
## Summary

Preserve Archive coverage and incremental indexing

## Work

1. Update RMEDO for reread coverage, incremental refresh, background audit preparation, and access to queryable CAPRMEDIO runtime data through DuckDB tables and `query_run`. Inventory the custom lookup indexes and identify which existing tables can replace them.
2. Review and fix RMEDO against the linked Code Synopses and the Epic decision record. Cover Atom metadata, relations, live Runs, query history, and diagnostics.
3. Implement and verify table access for the reviewed data. Replace custom lookup indexes with table queries wherever the table can serve the lookup.
4. Implement and verify compact Archive allocation lookups. Check the maximum Archived Version for IDs with a Current Atom or Draft, and the maximum Archived Atom number per Role across all archived IDs. Verify allocation with Archive bodies unloaded.
5. Verify selected Archives remain queryable on demand, ordinary refresh stays targeted, and performance guards pass. Use the existing Atom ID and Version comments to find the implementing modules and refresh their pins.

## Implementation entry points

- `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_WORKBENCH_BACKEND/service.py`
- `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_WORKBENCH_BACKEND/source_reader.py`
- `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/workbench_tools.py`
