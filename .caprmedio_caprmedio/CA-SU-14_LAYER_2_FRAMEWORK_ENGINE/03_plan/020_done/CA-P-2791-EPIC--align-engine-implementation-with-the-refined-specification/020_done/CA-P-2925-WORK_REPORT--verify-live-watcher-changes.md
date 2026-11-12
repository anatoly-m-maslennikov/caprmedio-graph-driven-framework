---
identity:
  id: CA-P-2925
  ref_id: CA-P-2925
context:
  container:
    atom: CA-P-2791
  role: Plan
  form: Work Report
  label: Work Report
  topics:
    main_subject: MODEL//CAPRMEDIO <+ Atom
  tier: 4
state:
  status: Done
  version: 1
  updated_at: 2026-11-11 03:05:37 +0400
destination:
  file:
    name: CA-P-2925-WORK_REPORT--verify-live-watcher-changes.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/020_done/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-2813
author: Anatoly Maslennikov
---

## Summary

Verify live watcher changes

## Details

Both retained real-project canaries passed against image c6e5cfb3e431, version 0.4.4.40. Atom create/update/rename/move/delete took 0.312–0.438 s; Scope Declaration structural phases took 12.997–14.591 s. Timers now start before mutation, including the child Atom checks during Scope movement/rename. The mixed batch of ten updates plus two Current Method and two Draft deletions passed in 0.284 s, with syncing=false and no reread. All owned carriers and indexed rows were cleaned up. C712 is Resolved; P2813 remains Active for remaining contract/pin and model checks. This is watcher acceptance, not Workflow-engine or full throughput/resource acceptance.

Evidence: .caprmedio_tmp/CA-P-2791/CA-P-2813/live-canary/latest.json, live-mixed-canary/mixed-latest.json and their corrected-timings logs. Reviewed delta key union and transactional delete/insert in projection_delta.py; ruff passed for the retained canary files.
