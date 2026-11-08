---
identity:
  id: CA-P-2751
  ref_id: CA-P-2751
context:
  container:
    atom: CA-P-2715
  role: Plan
  form: Work Report
  label: Work Report
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 4
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-2718
state:
  status: Done
  version: 2
  updated_at: 2026-11-09 00:18:04 +0400
destination:
  file:
    name: CA-P-2751-WORK_REPORT--generate-the-canonical-relation-registry-from-declarations.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes
author: Anatoly Maslennikov
---

## Summary

Generate the canonical relation registry from declarations

## Details

The deterministic source compiler and bounded incremental relation state are implemented. The installed 0.4.4.39 registry matches the source compilation. The asset has 47 names and 49 source pins; ordinary deltas do not reparse unchanged declarations.
