---
identity:
  id: CA-P-2755
  ref_id: CA-P-2755
context:
  container:
    atom: CA-P-2730
  role: Plan
  form: Work Report
  label: Work Report
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 4
state:
  status: Done
  version: 2
  updated_at: 2026-11-09 01:40:38 +0400
destination:
  file:
    name: CA-P-2755-WORK_REPORT--fix-moved-directory-indexing.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes/15-CA-P-2730-TASK--implement-and-refactor-the-accepted-specification
author: Anatoly Maslennikov
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-2754
---

## Summary

Fix moved-directory indexing

## Details

The destination-directory watcher fix covers both native directory flags and misreported flags, while refusing traversal outside the source root. Eleven watcher tests and the full 5,000-plus-500 Docker gate pass: batch move 8.128 seconds; 12 watcher mutations 240.0–340.6 ms. No gate was relaxed and the 500-Atom real benchmark corpus was preserved. Final deployment/live canary remain P2731.
