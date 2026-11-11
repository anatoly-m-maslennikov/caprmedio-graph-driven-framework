---
identity:
  id: CA-P-2751
  ref_id: CA-P-2751@1
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
  status: Archived
  version: 1
  updated_at: 2026-11-08 21:10:44 +0400
destination:
  file:
    name: CA-P-2751@1-WORK_REPORT--generate-the-canonical-relation-registry-from-declarations.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes/archived
author: Anatoly Maslennikov
---

## Summary

Generate the canonical relation registry from declarations

## Details

Implemented the first registry/materialization and generator slice. Initial67focused and31connected checks passed. Independent Sol High review then found missing-source canonical-edge retention, an ordinary full-support scan, conditional-metadata admission and incomplete source provenance. These are being fixed before acceptance. No generator release or final conformance is claimed.
