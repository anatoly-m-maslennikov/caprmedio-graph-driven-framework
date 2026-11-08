---
identity:
  id: CA-P-2718
  ref_id: CA-P-2718
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
  status: Active
  version: 3
  updated_at: 2026-11-08 20:26:04 +0400
destination:
  file:
    name: 03-CA-P-2718-TASK--generate-the-canonical-relation-registry-from-declarations.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes
author: Anatoly Maslennikov
relations:
  IS_BLOCKED_BY:
  - CA-P-2735
---

## Summary

Generate the canonical relation registry from declarations

## Objective

An external rebuildable registry is generated from accepted declarations, without a separately maintained relation list.

## Working procedure

Before starting or continuing a Task or subtask, review its next work unit and fix missing inputs or acceptance criteria first. If confidence is below 90%, re-read the Operator input. If still below 90%, ask the Operator and continue independent unblocked work.

Keep one small P / Work Report per Task and update it during execution. Until the shared Work Report model is adopted, reports are explicitly provisional and do not claim model or runtime adoption.

## Details

Subtasks below are work units, each with an estimated 10–20 minutes. Split a larger unit before starting it. For Atom batches, select a small number that fits the time box and repeat by batch; do not treat the whole inventory as one subtask. Assign at most one Scope Unit to each worker. Terra and Luna may handle bounded work; main judgments and final review use GPT-6.1 Sol at High effort.

## Subtasks

- [ ] Review the accepted generation RMEDO and gather applicable Method Policies. (ETA: 10–20 min per work unit.)
- [ ] Implement the reviewed REDO and non-Policy M; reuse an existing generator where it fits. (ETA: 10–20 min per work unit.)
- [ ] Verify deterministic generation, supported declaration Forms, aliases and diagnostics. (ETA: 10–20 min per work unit.)

## Acceptance

An external rebuildable registry is generated from accepted declarations, without a separately maintained relation list.
