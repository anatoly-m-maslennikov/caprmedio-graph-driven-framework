---
identity:
  id: CA-P-2940
  ref_id: CA-P-2940
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
  updated_at: 2026-11-11 06:42:51 +0400
destination:
  file:
    name: CA-P-2940-WORK_REPORT--verify-query-delivery-and-bookmark-failures.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-2852
  - CA-P-2813
author: Anatoly Maslennikov
---

## Summary

Verify query delivery and Bookmark failures

## Details

Image d520960c81eb passed HTTP/MCP full exports, stable pages, CTE preview, Check metadata, and Bookmark success/failure. Read-only disposable export and Journal mounts produced partial results on both interfaces. Completed query IDs still returned the exact rows.

Browser handling of the partial save and the remaining Evaluation checklist are open. Evidence: `.caprmedio_tmp/CA-P-2791/CA-P-2852/acceptance-d520/`.
