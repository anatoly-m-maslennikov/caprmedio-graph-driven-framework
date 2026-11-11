---
identity:
  id: CA-P-2758
  ref_id: CA-P-2758
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
  - CA-P-2721
state:
  status: Done
  version: 1
  updated_at: 2026-11-09 00:18:04 +0400
destination:
  file:
    name: CA-P-2758-WORK_REPORT--verify-and-release-the-relation-fixes.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/020_done/CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes/020_done
author: Anatoly Maslennikov
---

## Summary

Verify and release the relation fixes

## Details

Local release 003 deployed 0.4.4.39 with 218 selected checks passing. Installed registry bytes and native direct/derived relation queries were verified. Safe image cleanup remains pending. The separately found moved-directory defect is tracked by P2754; this report does not claim every E2E or the schema changes are released.
