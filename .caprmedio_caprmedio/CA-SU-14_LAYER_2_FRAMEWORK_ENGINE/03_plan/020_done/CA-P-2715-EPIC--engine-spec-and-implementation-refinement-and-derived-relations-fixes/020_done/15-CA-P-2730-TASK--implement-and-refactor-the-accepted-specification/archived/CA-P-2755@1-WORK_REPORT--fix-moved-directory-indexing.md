---
identity:
  id: CA-P-2755
  ref_id: CA-P-2755@1
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
  status: Archived
  version: 1
  updated_at: 2026-11-08 23:48:43 +0400
destination:
  file:
    name: CA-P-2755@1-WORK_REPORT--fix-moved-directory-indexing.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes/15-CA-P-2730-TASK--implement-and-refactor-the-accepted-specification/archived
author: Anatoly Maslennikov
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-2754
---

## Summary

Fix moved-directory indexing

## Details

The 5,000-plus-500 fixture exposed missing destination indexing. A bounded destination-watch fix passed the full performance gate; review then caught and corrected outside-tree traversal. Eleven watcher tests pass. Independent review accepted the boundary fix. The fix is not yet deployed; final release and verification remain.
