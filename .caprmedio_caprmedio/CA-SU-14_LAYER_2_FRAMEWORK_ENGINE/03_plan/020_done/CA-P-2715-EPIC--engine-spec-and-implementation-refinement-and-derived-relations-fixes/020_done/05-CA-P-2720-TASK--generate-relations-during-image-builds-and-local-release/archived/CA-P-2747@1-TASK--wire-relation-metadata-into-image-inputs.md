---
identity:
  id: CA-P-2747
  ref_id: CA-P-2747@1
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
  status: Archived
  version: 1
  updated_at: 2026-11-08 21:07:44 +0400
destination:
  file:
    name: CA-P-2747@1-TASK--wire-relation-metadata-into-image-inputs.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes/05-CA-P-2720-TASK--generate-relations-during-image-builds-and-local-release/archived
author: Anatoly Maslennikov
---

## Summary

Wire relation metadata into image inputs

## Details

Prepare the independently ready image-input slice of CA-P-2720 against adopted relation delivery RMEDO. Final generator acceptance and full release remain with the parent Task and its prerequisites.

- [ ] Review the accepted inputs and connected image callers. (ETA: 15–20 min.)
- [ ] Update the image-input implementation in its owning Scope Unit. (ETA: 15–20 min per slice.)
- [ ] Verify the changed paths with focused tests and report the handoff. (ETA: 15–20 min.)
