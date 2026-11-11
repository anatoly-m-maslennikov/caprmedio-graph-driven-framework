---
identity:
  id: CA-P-2993
  ref_id: CA-P-2993
context:
  container:
    atom: CA-P-2791
  role: Plan
  form: Work Report
  label: Work Report
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 4
state:
  status: Done
  version: 1
  updated_at: 2026-11-11 18:34:07 +0400
destination:
  file:
    name: CA-P-2993-WORK_REPORT--verify-the-lifecycle-update-image-and-shared-backlog-input.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-2934
author: Anatoly Maslennikov
---

## Summary

Verify the lifecycle Update image and shared Backlog input

## Details

The Update candidate passed the six-Tool HTTP checks and all nine Workbench Docker checks. Single-file visibility took 0.24–0.34 seconds. The 500-Atom create, update, rename and move cases took 4.3–5.4 seconds. The Scope Unit rename took 24.3 seconds, the cold rebuild 25.4 seconds, and the short resource guard passed without an OOM.

CA-D-475@25 now places Backlog Plans in the owning Scope Unit Role folder or inside their direct Backlog parent’s matching directory. The build selects its Formal Claim by Main Subject and Delivery Role and compiles the shared Backlog directory. The new acceptance cases show that the current Engine omits logical Backlog children when it archives or closes a Plan without a companion directory. The pre-cutover candidate was held before activation.
