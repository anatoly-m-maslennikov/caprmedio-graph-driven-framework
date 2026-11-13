---
identity:
  atom_id: CA-P-3037
  ref_id: CA-P-3037
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
  - CA-A-1344@1
  - CA-A-1353@1
state:
  version: 1
  status: active
  updated_at: '2026-11-12T16:36:40.643304+00:00'
destination:
  file:
    name: CA-P-3037-TASK--select-declaration-refresh-inputs-through-the-predecessor-image.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-3029-EPIC--mcp-query-and-atom-lifecycle-refinement
---
## Summary

Select declaration refresh inputs through the predecessor image

## Work

1. Update RMEDO for predecessor selection and Workbench declaration asset integration. Coordinate the Workbench consumer boundary with CA-P-3022.
2. Review and fix RMEDO against the linked Code Synopses and the Epic decision record.
3. Implement the reviewed RMEDO and verify refresh and existing-asset builds and the Workbench handoff from CA-P-3022. Use the existing Atom ID and Version comments to identify the modules that implement the affected RMEDO and refresh their pins.

## Implementation entry points

- `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/docker/runtime_images.py`
- `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_WORKBENCH_BACKEND/declaration_cfel.py`
- `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/docker/image_relation_registry.py`
