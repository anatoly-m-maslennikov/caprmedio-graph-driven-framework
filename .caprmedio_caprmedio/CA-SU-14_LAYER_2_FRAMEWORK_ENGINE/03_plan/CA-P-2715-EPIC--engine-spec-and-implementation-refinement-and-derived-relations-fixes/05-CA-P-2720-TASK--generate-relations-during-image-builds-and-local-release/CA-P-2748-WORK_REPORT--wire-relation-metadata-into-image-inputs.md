---
identity:
  id: CA-P-2748
  ref_id: CA-P-2748
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
  - CA-P-2747
state:
  status: Active
  version: 1
  updated_at: 2026-11-08 21:07:44 +0400
destination:
  file:
    name: CA-P-2748-WORK_REPORT--wire-relation-metadata-into-image-inputs.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes/05-CA-P-2720-TASK--generate-relations-during-image-builds-and-local-release
author: Anatoly Maslennikov
---

## Summary

Wire relation metadata into image inputs

## Details

Reviewed the adopted delivery contract and every image-build entry point. The backend generator API is available; its independent correctness fixes remain with CA-P-2718. This child owns the image-input adapter work that can proceed against that explicit API. No image build, release or installed verification is claimed.
