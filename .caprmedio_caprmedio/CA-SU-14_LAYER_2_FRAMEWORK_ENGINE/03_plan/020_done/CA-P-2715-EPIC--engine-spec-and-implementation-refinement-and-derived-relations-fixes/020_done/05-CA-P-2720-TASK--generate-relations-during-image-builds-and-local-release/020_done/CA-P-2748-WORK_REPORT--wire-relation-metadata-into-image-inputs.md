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
  status: Done
  version: 2
  updated_at: 2026-11-09 00:18:04 +0400
destination:
  file:
    name: CA-P-2748-WORK_REPORT--wire-relation-metadata-into-image-inputs.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/020_done/CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes/020_done/05-CA-P-2720-TASK--generate-relations-during-image-builds-and-local-release/020_done
author: Anatoly Maslennikov
---

## Summary

Wire relation metadata into image inputs

## Details

The declaration-derived relation registry is a generated image input with deterministic fingerprinting and selected-Project binding. Fixture tests and installed 0.4.4.39 verification passed. New schema-image integration is tracked separately by P2752.
