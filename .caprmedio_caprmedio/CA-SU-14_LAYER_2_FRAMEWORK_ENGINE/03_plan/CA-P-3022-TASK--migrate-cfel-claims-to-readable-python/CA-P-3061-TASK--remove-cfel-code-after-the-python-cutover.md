---
identity:
  atom_id: CA-P-3061
  ref_id: CA-P-3061
context:
  role: plan
  form: Plan
  label: Task
  tier: 3
  container:
    atom: CA-P-3022
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//PROGRAMMATIC
relations:
  IS_BLOCKED_BY:
  - CA-P-3055
state:
  version: 1
  status: active
  updated_at: '2026-11-13T17:14:03.749993+00:00'
destination:
  file:
    name: CA-P-3061-TASK--remove-cfel-code-after-the-python-cutover.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-3022-TASK--migrate-cfel-claims-to-readable-python
---
## Summary

Remove CFEL code after the Python cutover

## Work

Move the remaining CFEL-dependent Workbench, Lifecycle, graph and build readers to the native Python Model from CA-P-3055 and the migrated Claims in CA-P-3022. Once their replacement inputs are ready, delete CFEL readers, parsers, compilers, Python-to-CFEL translation, and CFEL-only build hooks, tests and fixtures. Verify the image builds, the affected consumers work, and the build and runtime have no CFEL dependency.
