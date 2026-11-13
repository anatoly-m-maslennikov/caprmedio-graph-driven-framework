---
identity:
  atom_id: CA-P-3047
  ref_id: CA-P-3047
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
  - CA-A-1364@1
state:
  version: 1
  status: done
  updated_at: '2026-11-12T16:36:43.923478+00:00'
destination:
  file:
    name: CA-P-3047-TASK--return-saved-query-links-or-an-explicit-unavailable-reason.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-3029-EPIC--mcp-query-and-atom-lifecycle-refinement/020_done
---
## Summary

Return saved query links or an explicit unavailable reason

## Work

1. Update RMEDO for saved-query and saved View link responses.
2. Review and fix RMEDO against the linked Code Synopses and the Epic decision record.
3. Implement the reviewed RMEDO and verify configured links and null URLs with a reason when unavailable. Use the existing Atom ID and Version comments to identify the modules that implement the affected RMEDO and refresh their pins.

## Implementation entry points

- `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/registry_workbench_provider.py`
- `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/workbench_links.py`
- `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/shared_gateway.py`
