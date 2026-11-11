---
identity:
  atom_id: CA-P-3007
  ref_id: CA-P-3007
context:
  container:
    atom: CA-P-2791
  role: plan
  form: work_report
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 4
  label: Work Report
state:
  status: done
  version: 1
  updated_at: '2026-11-12T00:01:59.664109+04:00'
destination:
  file:
    name: CA-P-3007-WORK_REPORT--verify-live-atom-lifecycle-latency-and-scope-unit-refresh.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-3006
author: Anatoly Maslennikov
---

## Summary

Verify live Atom lifecycle latency and Scope Unit refresh

## Details

CA-P-3006. Local image `sha256:a72ddb581001e00ab529871736cc7ce399950e0baa82fbd89f8a36ccf08d0932`.

- Lifecycle used a Scope Unit created after MCP startup. Both seeded cases passed all six operations, form cancellation, stale-Version rejection, and cleanup in the same container.
- The replacement Update took 109.7 seconds. The same-ID Update took 78.2 seconds. Both returned within the original 180-second limit.
- The focused lifecycle tests and both Workbench Docker guards passed. Health, Workbench frontend and query, and MCP discovery passed on the activated image.
