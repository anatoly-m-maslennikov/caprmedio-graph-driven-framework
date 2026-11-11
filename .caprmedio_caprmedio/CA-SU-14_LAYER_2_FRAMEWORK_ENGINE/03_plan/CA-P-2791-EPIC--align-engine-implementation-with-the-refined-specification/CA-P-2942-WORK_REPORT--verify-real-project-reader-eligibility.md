---
identity:
  id: CA-P-2942
  ref_id: CA-P-2942
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
  updated_at: 2026-11-11 06:48:55 +0400
destination:
  file:
    name: CA-P-2942-WORK_REPORT--verify-real-project-reader-eligibility.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-2859
author: Anatoly Maslennikov
---

## Summary

Verify real Project reader eligibility

## Details

On isolated image d520960c81eb, HTTP and MCP query_run returned CA-C-525, CA-C-526 and CA-C-527 at their exact paths. Three native Core Formal Claims were queryable without adding Scope Unit rows. Archived carriers remained absent from the candidate projection.

Evidence: `.caprmedio_tmp/CA-P-2791/CA-P-2859/real-project-interface-provenance.json`.
