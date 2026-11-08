---
identity:
  id: CA-P-2720
  ref_id: CA-P-2720
context:
  container:
    atom: CA-P-2715
  role: Plan
  form: Plan
  label: Task
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 4
state:
  status: Backlog
  version: 2
  updated_at: 2026-11-08 19:15:36 +0400
destination:
  file:
    name: 05-CA-P-2720-TASK--generate-relations-during-image-builds-and-local-release.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes
author: Anatoly Maslennikov
relations:
  IS_BLOCKED_BY:
  - CA-P-2718
---

## Summary

Generate relations during image builds and local release

## Objective

Every supported image-build path regenerates the asset; local release uses that same path.

## Working procedure

Before starting or continuing a Task or subtask, review its next work unit and fix missing inputs or acceptance criteria first. If confidence is below 90%, re-read the Operator input. If still below 90%, ask the Operator and continue independent unblocked work.

Keep one small P / Work Report per Task and update it during execution. Until the shared Work Report model is adopted, reports are explicitly provisional and do not claim model or runtime adoption.

## Details

Subtasks below are work units, each with an estimated 10–20 minutes. Split a larger unit before starting it. For Atom batches, select a small number that fits the time box and repeat by batch; do not treat the whole inventory as one subtask. Assign at most one Scope Unit to each worker. Terra and Luna may handle bounded work; main judgments and final review use GPT-6.1 Sol at High effort.

## Subtasks

- [ ] Review the build and local-release entry points and the applicable RMEDO. (ETA: 10–20 min per work unit.)
- [ ] Wire generation into every image rebuild path, including local release. (ETA: 10–20 min per work unit.)
- [ ] Build with a changed declaration and verify that the image uses its generated registry. (ETA: 10–20 min per work unit.)

## Acceptance

Every supported image-build path regenerates the asset; local release uses that same path.
