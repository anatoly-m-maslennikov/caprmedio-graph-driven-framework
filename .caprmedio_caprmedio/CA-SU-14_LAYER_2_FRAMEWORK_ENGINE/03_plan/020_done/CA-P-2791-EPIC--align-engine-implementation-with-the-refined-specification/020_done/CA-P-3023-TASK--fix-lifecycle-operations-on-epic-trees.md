---
identity:
  atom_id: CA-P-3023
  ref_id: CA-P-3023
context:
  role: plan
  form: Plan
  label: Task
  tier: 4
  container:
    atom: CA-P-2791
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
state:
  version: 1
  status: done
  updated_at: '2026-11-12T01:56:22.847434+00:00'
destination:
  file:
    name: CA-P-3023-TASK--fix-lifecycle-operations-on-epic-trees.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/020_done/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done
---
## Summary

Fix lifecycle operations on Epic trees

## Objective

Implement and verify the lifecycle follow-up from CA-P-3018.

## Details

- Update the Engine RMEDO and review the affected lifecycle contracts.
- Fix the reported Epic status-change and content-update failures.
- Verify activation of a direct and a nested Task. Test the Draft-child regression independently.
- Record the results in a Work Report.