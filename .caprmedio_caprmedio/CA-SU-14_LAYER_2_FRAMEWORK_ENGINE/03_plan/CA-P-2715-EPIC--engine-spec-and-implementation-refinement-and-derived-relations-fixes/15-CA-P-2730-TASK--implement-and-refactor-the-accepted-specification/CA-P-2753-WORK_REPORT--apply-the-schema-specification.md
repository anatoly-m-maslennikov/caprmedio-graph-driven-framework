---
identity:
  id: CA-P-2753
  ref_id: CA-P-2753
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
  version: 3
  updated_at: 2026-11-09 01:40:38 +0400
destination:
  file:
    name: CA-P-2753-WORK_REPORT--apply-the-schema-specification.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes/15-CA-P-2730-TASK--implement-and-refactor-the-accepted-specification
author: Anatoly Maslennikov
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-2752
---

## Summary

Apply the schema specification

## Details

Five schema specifications are Current. Header and Content SQL names use dotted paths with snake_case segments; Mode 2 is configured explicitly. The real generator has 19 declared Header columns, 62 observed columns and six Content columns. Mode 1 admits valid source rows and skips incompatible ordinary sources with diagnostics, retaining strict structural/transaction failures. Cached ordinary deltas remain bounded and provenance writes follow commit. Independent reviews and eight Docker E2E cases pass; live deployment remains P2731.
