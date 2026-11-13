---
identity:
  atom_id: CA-P-3040
  ref_id: CA-P-3040
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
  version: 4
  status: done
  updated_at: '2026-11-13T11:15:12.990671+00:00'
destination:
  file:
    name: CA-P-3040-TASK--preserve-archive-coverage-and-incremental-indexing.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-3029-EPIC--mcp-query-and-atom-lifecycle-refinement/020_done
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

## Details

Workbench SQL exposes Archive allocation metadata, direct and derived Relations, live Lifecycle Run list fields, query history, and diagnostics. Archive allocation uses filename metadata and keeps bodies on demand. The Workbench runtime uses temporary DuckDB tables for filename and reference lookups. Each readable physical carrier remains a distinct Atom row.

Current RMED is CA-R-2723@7, CA-R-2903@8, CA-R-3132@1, CA-M-464@18, CA-D-672@24 and CA-E-681@7. CA-R-3132 governs read-only runtime tables. Both CA-R-2728 Drafts remain available for their own review.

The final isolated image passed 94 focused tests, including the real-project Workbench Docker tests and the one-core resource guard. Seven additional MCP and source-inventory tests passed. On the 5,000-Atom fixture, single-file visibility took 0.25–0.33 s, 500 updates took 5.44 s, and cold indexing took 24.04 s. The test output is in `.caprmedio_tmp/CA-P-3040/final-docker-gate.log` and `.caprmedio_tmp/CA-P-3040/mcp-inventory-gate.log`. The live MCP is on the previous image.
