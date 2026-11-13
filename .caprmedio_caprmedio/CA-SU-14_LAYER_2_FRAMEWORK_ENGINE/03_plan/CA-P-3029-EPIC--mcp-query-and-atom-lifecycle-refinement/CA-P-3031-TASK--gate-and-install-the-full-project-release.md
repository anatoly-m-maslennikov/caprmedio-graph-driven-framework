---
identity:
  atom_id: CA-P-3031
  ref_id: CA-P-3031
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
  - CA-A-1365@1
  - CA-A-1366@1
  - CA-A-1375@1
  - CA-A-1352@1
state:
  version: 1
  status: active
  updated_at: '2026-11-12T16:36:33.559467+00:00'
destination:
  file:
    name: CA-P-3031-TASK--gate-and-install-the-full-project-release.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-3029-EPIC--mcp-query-and-atom-lifecycle-refinement
---
## Summary

Gate and install the full Project release

## Work

1. Update RMEDO for Local Release test gates, package scope, staging, installation, and image retention.
2. Review and fix RMEDO against the linked Code Synopses and the Epic decision record.
3. Implement the reviewed RMEDO and verify full-suite gating, temporary staging, healthy replacement, package contents, and retention of one previous image. Use the existing Atom ID and Version comments to identify the modules that implement the affected RMEDO and refresh their pins.

## Implementation entry points

- `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/project_mcp_bootstrap.py`
- `LAYER_5_FRAMEWORK_DELIVERY/RELEASE_VERSION/local_release.py`
- `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/COMPILE_APPLICABLE_METHODOLOGY/compile_applicable_methodology.py`
