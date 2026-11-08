---
identity:
  id: CA-P-2749
  ref_id: CA-P-2749
context:
  container:
    atom: CA-P-2720
  role: Plan
  form: Plan
  label: Task
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 4
relations:
  IS_BLOCKED_BY:
  - CA-P-2735
state:
  status: Active
  version: 1
  updated_at: 2026-11-08 21:10:44 +0400
destination:
  file:
    name: CA-P-2749-TASK--wire-relation-metadata-into-release-packages.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes/05-CA-P-2720-TASK--generate-relations-during-image-builds-and-local-release
author: Anatoly Maslennikov
---

## Summary

Wire relation metadata into release packages

## Details

Prepare the independently ready package/full-suite adapter slice against adopted delivery RMEDO. The parent Task owns final integration and release verification.

- [ ] Review the selected package and full-suite callers. (ETA: 15–20 min.)
- [ ] Update the owning Project Tools implementation. (ETA: 15–20 min per slice.)
- [ ] Verify focused checks and report the integration handoff. (ETA: 15–20 min.)
