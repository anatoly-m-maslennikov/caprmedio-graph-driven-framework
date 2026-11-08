---
identity:
  id: CA-P-2730
  ref_id: CA-P-2730
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
    name: 15-CA-P-2730-TASK--implement-and-refactor-the-accepted-specification.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes
author: Anatoly Maslennikov
relations:
  IS_BLOCKED_BY:
  - CA-P-2729
---

## Summary

Implement and refactor the accepted specification

## Objective

Accepted changes are implemented and reviewed with traceable versioned Atom IDs; old code is removed only where the accepted spec requires it.

## Working procedure

Before starting or continuing a Task or subtask, review its next work unit and fix missing inputs or acceptance criteria first. If confidence is below 90%, re-read the Operator input. If still below 90%, ask the Operator and continue independent unblocked work.

Keep one small P / Work Report per Task and update it during execution. Until the shared Work Report model is adopted, reports are explicitly provisional and do not claim model or runtime adoption.

## Details

Subtasks below are work units, each with an estimated 10–20 minutes. Split a larger unit before starting it. For Atom batches, select a small number that fits the time box and repeat by batch; do not treat the whole inventory as one subtask. Assign at most one Scope Unit to each worker. Terra and Luna may handle bounded work; main judgments and final review use GPT-6.1 Sol at High effort.

## Subtasks

- [ ] Review and fix the next task, then compile the applicable PROGRAMMATIC-to-local Method Policies into one reusable prompt. (ETA: 10–20 min per work unit.)
- [ ] Verify that every required specification correction is promoted and rebaselined. Gather the accepted REDO plus non-Policy M and implement one scope-local work unit. (ETA: 10–20 min per work unit.)
- [ ] Review and fix the change; add meaningful E2E coverage and update the small Work Report. (ETA: 10–20 min per work unit.)

## Acceptance

Accepted changes are implemented and reviewed with traceable versioned Atom IDs; old code is removed only where the accepted spec requires it.
