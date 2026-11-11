---
identity:
  id: CA-P-2750
  ref_id: CA-P-2750@1
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
  status: Archived
  version: 1
  updated_at: 2026-11-08 21:10:44 +0400
destination:
  file:
    name: CA-P-2750@1-WORK_REPORT--wire-relation-metadata-into-release-packages.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes/05-CA-P-2720-TASK--generate-relations-during-image-builds-and-local-release/archived
author: Anatoly Maslennikov
---

## Summary

Wire relation metadata into release packages

## Details

Reviewed package preparation and image-build caller seams. The backend generator CLI is available; independent correctness review remains with P2718. Package generation and image integration will reuse that compiler. No image build, installation or release is claimed.
