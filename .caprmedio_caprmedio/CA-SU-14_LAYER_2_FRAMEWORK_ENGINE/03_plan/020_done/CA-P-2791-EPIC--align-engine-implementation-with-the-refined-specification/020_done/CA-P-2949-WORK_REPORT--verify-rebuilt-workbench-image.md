---
identity:
  id: CA-P-2949
  ref_id: CA-P-2949
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
  updated_at: 2026-11-11 07:29:57 +0400
destination:
  file:
    name: CA-P-2949-WORK_REPORT--verify-rebuilt-workbench-image.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/020_done/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-2813
  - CA-P-2866
author: Anatoly Maslennikov
---

## Summary

Verify rebuilt Workbench image

## Details

The 87f745f425bc image loaded schema v2, served the frontend, returned seven declared Content columns and exposed three native Formal Claims. HTTP and MCP both accepted a graph query ending in a line comment and returned the expected uncapped and preview results. All six changed backend module hashes match the build context.

Scope refresh memory and two-image declaration acceptance remain open. Evidence: `.caprmedio_tmp/CA-P-2791/CA-P-2866/formal-input-20261111/image-build-ancestry-v2/`.
