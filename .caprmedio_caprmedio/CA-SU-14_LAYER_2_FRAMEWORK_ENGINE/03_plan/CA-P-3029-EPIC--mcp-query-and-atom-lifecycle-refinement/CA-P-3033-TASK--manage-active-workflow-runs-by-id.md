---
identity:
  atom_id: CA-P-3033
  ref_id: CA-P-3033
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
  - CA-A-1354@1
  - CA-A-1348@1
state:
  version: 1
  status: active
  updated_at: '2026-11-12T16:36:39.379548+00:00'
destination:
  file:
    name: CA-P-3033-TASK--manage-active-workflow-runs-by-id.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-3029-EPIC--mcp-query-and-atom-lifecycle-refinement
---
## Summary

Manage active Workflow Runs by ID

## Work

1. Update RMEDO for active Run discovery, session ownership, cross-session continuation, and input correction.
2. Review and fix RMEDO against the linked Code Synopses and the Epic decision record.
3. Implement the reviewed RMEDO and verify session and Project listings, operation by Run ID, and retention of valid fields. Use the existing Atom ID and Version comments to identify the modules that implement the affected RMEDO and refresh their pins.

## Implementation entry points

- `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/registry_lifecycle_provider.py`
- `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/direct_gateway.py`
- `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/tool_registry_runtime.py`
