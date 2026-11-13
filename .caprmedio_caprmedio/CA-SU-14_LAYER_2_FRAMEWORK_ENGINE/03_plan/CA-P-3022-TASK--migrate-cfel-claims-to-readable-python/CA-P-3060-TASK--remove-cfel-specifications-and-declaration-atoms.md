---
identity:
  atom_id: CA-P-3060
  ref_id: CA-P-3060
context:
  role: plan
  form: Plan
  label: Task
  tier: 3
  container:
    atom: CA-P-3022
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
state:
  version: 1
  status: active
  updated_at: '2026-11-13T17:14:01.288598+00:00'
destination:
  file:
    name: CA-P-3060-TASK--remove-cfel-specifications-and-declaration-atoms.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-3022-TASK--migrate-cfel-claims-to-readable-python
---
## Summary

Remove CFEL specifications and Declaration Atoms

## Work

After the surviving Claims and Subject notation rules have Python or Subject-specific authority, activate the Python-only CA-R-2721 revision. Remove CFEL-only RMEDO and obsolete CFEL Declaration carriers from the Current and Draft source sets, including the CFEL definition, operator, construct, and function Declarations. Preserve graph Relations and other rules that still apply by moving their authority before removing the CFEL sources. Check CA-R-2471, CA-R-2487, and CA-R-2563 explicitly. Verify no live Declaration or Topic depends on the retired CFEL branch.
