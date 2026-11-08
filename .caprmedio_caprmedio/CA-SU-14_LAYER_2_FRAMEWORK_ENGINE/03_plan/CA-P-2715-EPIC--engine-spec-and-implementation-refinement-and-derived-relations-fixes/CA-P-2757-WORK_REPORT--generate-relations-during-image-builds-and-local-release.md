---
identity:
  id: CA-P-2757
  ref_id: CA-P-2757
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
  - CA-P-2720
state:
  status: Done
  version: 1
  updated_at: 2026-11-09 00:18:04 +0400
destination:
  file:
    name: CA-P-2757-WORK_REPORT--generate-relations-during-image-builds-and-local-release.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes
author: Anatoly Maslennikov
---

## Summary

Generate relations during image builds and local release

## Details

Image and local-release paths regenerate canonical relation metadata, seal it in input identity and reject missing or failed generation. Local release 003 installed 0.4.4.39. Schema-asset additions remain separate unfinished work under P2752.
