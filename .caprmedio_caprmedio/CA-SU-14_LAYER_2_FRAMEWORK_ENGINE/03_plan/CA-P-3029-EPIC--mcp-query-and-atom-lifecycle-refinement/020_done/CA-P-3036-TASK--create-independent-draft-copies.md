---
identity:
  atom_id: CA-P-3036
  ref_id: CA-P-3036
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
  - CA-A-1340@2
state:
  version: 1
  status: done
  updated_at: '2026-11-12T16:36:40.391394+00:00'
destination:
  file:
    name: CA-P-3036-TASK--create-independent-draft-copies.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-3029-EPIC--mcp-query-and-atom-lifecycle-refinement/020_done
---
## Summary

Create independent Draft copies

## Work

1. Update RMEDO for independent Draft creation from an existing Atom.
2. Review and fix RMEDO against the linked Code Synopses and the Epic decision record.
3. Implement the reviewed RMEDO and verify a fresh ID at Version 1, copied relations, and source preservation. Use the existing Atom ID and Version comments to identify the modules that implement the affected RMEDO and refresh their pins.

## Implementation entry points

- `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/registry_lifecycle_provider.py`
- `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/ATOM_LIFECYCLE/draft.py`
- `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/tests/test_lifecycle_live_performance_canary.py`
