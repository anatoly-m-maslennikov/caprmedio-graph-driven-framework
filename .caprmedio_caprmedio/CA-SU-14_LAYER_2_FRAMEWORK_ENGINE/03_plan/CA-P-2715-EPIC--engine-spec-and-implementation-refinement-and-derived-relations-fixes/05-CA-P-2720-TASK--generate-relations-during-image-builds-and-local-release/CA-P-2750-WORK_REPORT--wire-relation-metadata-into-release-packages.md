---
identity:
  id: CA-P-2750
  ref_id: CA-P-2750
context:
  container:
    atom: CA-P-2720
  role: Plan
  form: Work Report
  label: Work Report
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 4
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-2749
state:
  status: Done
  version: 2
  updated_at: 2026-11-09 00:18:04 +0400
destination:
  file:
    name: CA-P-2750-WORK_REPORT--wire-relation-metadata-into-release-packages.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes/05-CA-P-2720-TASK--generate-relations-during-image-builds-and-local-release
author: Anatoly Maslennikov
---

## Summary

Wire relation metadata into release packages

## Details

Release packaging generates and seals canonical relation metadata before image construction. Missing, failed and unsafe outputs are rejected. Local release 003 verified the installed asset. New schema-package integration remains under P2752.
