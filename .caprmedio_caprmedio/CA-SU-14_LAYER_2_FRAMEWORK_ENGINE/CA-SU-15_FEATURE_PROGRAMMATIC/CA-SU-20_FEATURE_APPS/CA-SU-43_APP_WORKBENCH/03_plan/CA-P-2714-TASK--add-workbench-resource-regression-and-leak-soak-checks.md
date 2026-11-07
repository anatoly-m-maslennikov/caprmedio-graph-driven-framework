---
atom_id: CA-P-2714
ref_id: CA-P-2714
container:
  scope_unit: CA-SU-43
role: Plan
form: Plan
label: Task
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
tier: 3
status: Done
version: 3
updated_at: 2026-11-07 14:47:29 +0000
carrier_destination:
  file:
    name: CA-P-2714-TASK--add-workbench-resource-regression-and-leak-soak-checks.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/03_plan
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---

## Summary

Add Workbench resource regression and leak soak checks

## Objective

Add and verify the resource and leak checks defined by CA-M-508, CA-E-799 and CA-E-800.

## Tasks

- [x] Create, review and adopt RMED.
- [x] Reuse the applicable Method Policy prompt.
- [x] Implement and review the accepted RMED.
- [x] Calibrate and freeze resource limits.
- [x] Run the resource guard and unchanged performance gates.
- [x] Run the 30-minute soak and fix confirmed leaks.
- [x] Record evidence and limitations.

## Results

Completed. See [acceptance report](CA-P-2714-TASK--add-workbench-resource-regression-and-leak-soak-checks/report.md). The resource-test pass did not deploy changes. The subsequent local release installed and verified version 0.4.4.35; see the linked report.
