---
identity:
  id: CA-P-2727
  ref_id: CA-P-2727
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
  status: Done
  version: 3
  updated_at: 2026-11-09 00:18:04 +0400
destination:
  file:
    name: 12-CA-P-2727-TASK--promote-the-reviewed-specification-drafts.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/020_done/CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes/020_done
author: Anatoly Maslennikov
relations:
  IS_BLOCKED_BY:
  - CA-P-2726
  - CA-P-2722
  - CA-P-2721
---

## Summary

Promote the reviewed specification Drafts

## Objective

All approved Drafts are Current or explicitly held; preserved history and actual promotion results are checked.

## Working procedure

Before starting or continuing a Task or subtask, review its next work unit and fix missing inputs or acceptance criteria first. If confidence is below 90%, re-read the Operator input. If still below 90%, ask the Operator and continue independent unblocked work.

Keep one small P / Work Report per Task and update it during execution. Until the shared Work Report model is adopted, reports are explicitly provisional and do not claim model or runtime adoption.

## Details

Subtasks below are work units, each with an estimated 10–20 minutes. Split a larger unit before starting it. For Atom batches, select a small number that fits the time box and repeat by batch; do not treat the whole inventory as one subtask. Assign at most one Scope Unit to each worker. Terra and Luna may handle bounded work; main judgments and final review use GPT-6.1 Sol at High effort.

## Subtasks

- [ ] Review the next promotion batch and verify its exact Current predecessors. (ETA: 10–20 min per work unit.)
- [ ] Promote or replace the reviewed Atoms and preserve predecessor history. (ETA: 10–20 min per work unit.)
- [ ] Verify replacement links, identity, ownership and complete thin-index coverage. (ETA: 10–20 min per work unit.)

## Acceptance

All approved Drafts are Current or explicitly held; preserved history and actual promotion results are checked.
