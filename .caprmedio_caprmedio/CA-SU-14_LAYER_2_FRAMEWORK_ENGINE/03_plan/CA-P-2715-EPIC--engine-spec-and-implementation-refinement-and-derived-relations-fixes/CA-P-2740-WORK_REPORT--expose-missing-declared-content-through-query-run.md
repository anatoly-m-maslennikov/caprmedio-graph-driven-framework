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
  status: Done
  version: 4
  updated_at: 2026-11-09 01:40:38 +0400
destination:
  file:
    name: CA-P-2740-WORK_REPORT--expose-missing-declared-content-through-query-run.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes
author: Anatoly Maslennikov
---

## Summary

Expose missing declared Content through query_run

## Details

Operation Declaration and reader corrections expose the supported declared Content through query_run. The 78 unavailable legacy Atoms remain explicitly deferred. The new literal schema generator reads Current Header and Content Declarations; Mode 2 remains factual Headers plus declared Content. No atom_document or raw-source SQL escape was added.
