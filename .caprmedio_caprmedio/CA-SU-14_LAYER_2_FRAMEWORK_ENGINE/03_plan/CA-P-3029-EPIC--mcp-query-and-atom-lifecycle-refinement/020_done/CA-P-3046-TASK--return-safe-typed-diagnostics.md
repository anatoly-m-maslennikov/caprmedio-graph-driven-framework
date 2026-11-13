---
identity:
  atom_id: CA-P-3046
  ref_id: CA-P-3046
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
  - CA-A-1346@1
  - CA-A-1363@1
  - CA-A-1374@1
state:
  version: 1
  status: done
  updated_at: '2026-11-12T16:36:43.556733+00:00'
destination:
  file:
    name: CA-P-3046-TASK--return-safe-typed-diagnostics.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-3029-EPIC--mcp-query-and-atom-lifecycle-refinement/020_done
---
## Summary

Return safe typed diagnostics

## Work

1. Update RMEDO for query diagnostics, typed failures, and diagnostic failures.
2. Review and fix RMEDO against the linked Code Synopses and the Epic decision record.
3. Implement the reviewed RMEDO and verify safe SQL errors and retained primary and secondary failures. Use the existing Atom ID and Version comments to identify the modules that implement the affected RMEDO and refresh their pins.

## Implementation entry points

- `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_WORKBENCH_BACKEND/query_store.py`
- `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/shared_gateway.py`
- `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/workbench_tools.py`
