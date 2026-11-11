---
identity:
  id: CA-P-2964
  ref_id: CA-P-2964
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
  updated_at: 2026-11-11 08:51:05 +0400
destination:
  file:
    name: CA-P-2964-WORK_REPORT--verify-installed-workbench-and-query_run.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/020_done/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-2818
author: Anatoly Maslennikov
---

## Summary

Verify installed Workbench and query_run

## Details

Local Release installed Workbench 0.4.4.43 as image `sha256:1d89cc9b99869d1fc4d42c38cd0bf7790c1bad4a7098a3ceb3bcd640a1b2fb60`. Focused validation ran 64 modules and 566 cases, with two skips and no failed modules.

The installed HTTP and MCP query_run interfaces agree on seven declared Content columns, three native Formal Claims, and both directions of containment. query_run also lists all five Methodology Scope Units. The release removed the superseded Project-owned container and three obsolete Project-owned images. Its receipt retains cleanup pending for images without verified ownership.

The release receipt is `.caprmedio_runtime/simple_local_release/reports/engine-refinement-20261111-v5.md`. Installed proof is in `.caprmedio_tmp/CA-P-2791/CA-P-2818/installed-acceptance-v5.json`.
