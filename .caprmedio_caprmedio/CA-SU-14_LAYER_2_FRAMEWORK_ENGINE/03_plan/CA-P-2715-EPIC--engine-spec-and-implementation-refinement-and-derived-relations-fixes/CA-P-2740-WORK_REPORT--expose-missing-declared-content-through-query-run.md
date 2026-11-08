---
identity:
  id: CA-P-2740
  ref_id: CA-P-2740
context:
  container:
    atom: CA-P-2715
  role: Plan
  form: Work Report
  label: Work Report
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom.Content
  tier: 4
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-2736
state:
  status: Active
  version: 1
  updated_at: 2026-11-08 19:15:36 +0400
destination:
  file:
    name: CA-P-2740-WORK_REPORT--expose-missing-declared-content-through-query-run.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes
author: Anatoly Maslennikov
---

## Summary

Expose missing declared Content through query_run

## Details

Found a source-declaration gap and a generic Markdown extraction bug. New Operation Declaration CA-R-970308623@1 passed two independent Sol High reviews and is Current; content.operation is queryable but legacy nested text needs the reviewed extractor fix. Content16, nested-header13 and schema-refresh4 tests pass. The extractor fix passed independent re-review after two corrections. Local release and full live-content verification remain.
