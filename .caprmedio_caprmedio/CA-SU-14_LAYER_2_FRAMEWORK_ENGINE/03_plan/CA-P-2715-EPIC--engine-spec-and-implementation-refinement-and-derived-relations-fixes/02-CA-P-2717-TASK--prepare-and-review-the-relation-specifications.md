---
identity:
  id: CA-P-2717
  ref_id: CA-P-2717
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
  updated_at: 2026-11-08 20:22:21 +0400
destination:
  file:
    name: 02-CA-P-2717-TASK--prepare-and-review-the-relation-specifications.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes
author: Anatoly Maslennikov
relations:
  IS_BLOCKED_BY:
  - CA-P-2716
---

## Summary

Prepare and review the relation specifications

## Objective

The reviewed relation RMEDO covers canonical registry generation, inverse aliases and consumer behavior without changing source relation facts silently.

## Working procedure

Before starting or continuing a Task or subtask, review its next work unit and fix missing inputs or acceptance criteria first. If confidence is below 90%, re-read the Operator input. If still below 90%, ask the Operator and continue independent unblocked work.

Keep one small P / Work Report per Task and update it during execution. Until the shared Work Report model is adopted, reports are explicitly provisional and do not claim model or runtime adoption.

## Details

Subtasks below are work units, each with an estimated 10–20 minutes. Split a larger unit before starting it. For Atom batches, select a small number that fits the time box and repeat by batch; do not treat the whole inventory as one subtask. Assign at most one Scope Unit to each worker. Terra and Luna may handle bounded work; main judgments and final review use GPT-6.1 Sol at High effort.

## Subtasks

- [ ] Read all Current relation declarations and compare them with the consumer. (ETA: 10–20 min per work unit.)
- [ ] Create or update RMEDO Drafts for the confirmed gaps; use IS_REPLACEMENT_FOR for replacement proposals. (ETA: 10–20 min per work unit.)
- [ ] Review and fix the relation packet against active declarations and the latest Operator input. (ETA: 10–20 min per work unit.)

## Acceptance

The reviewed relation RMEDO covers canonical registry generation, inverse aliases and consumer behavior without changing source relation facts silently.
