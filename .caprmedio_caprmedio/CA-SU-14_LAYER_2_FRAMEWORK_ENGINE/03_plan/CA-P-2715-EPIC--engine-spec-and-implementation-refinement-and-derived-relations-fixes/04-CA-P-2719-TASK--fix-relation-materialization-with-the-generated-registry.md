---
identity:
  id: CA-P-2719
  ref_id: CA-P-2719
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
    name: 04-CA-P-2719-TASK--fix-relation-materialization-with-the-generated-registry.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes
author: Anatoly Maslennikov
relations:
  IS_BLOCKED_BY:
  - CA-P-2718
---

## Summary

Fix relation materialization with the generated registry

## Objective

The tested consumer matches the accepted declarations; source issues and unsupported qualified derivations are explicitly resolved or held.

## Working procedure

Before starting or continuing a Task or subtask, review its next work unit and fix missing inputs or acceptance criteria first. If confidence is below 90%, re-read the Operator input. If still below 90%, ask the Operator and continue independent unblocked work.

Keep one small P / Work Report per Task and update it during execution. Until the shared Work Report model is adopted, reports are explicitly provisional and do not claim model or runtime adoption.

## Details

Subtasks below are work units, each with an estimated 10–20 minutes. Split a larger unit before starting it. For Atom batches, select a small number that fits the time box and repeat by batch; do not treat the whole inventory as one subtask. Assign at most one Scope Unit to each worker. Terra and Luna may handle bounded work; main judgments and final review use GPT-6.1 Sol at High effort.

## Subtasks

- [ ] Review the next implementation slice and its accepted RMEDO. (ETA: 10–20 min per work unit.)
- [ ] Integrate registry-based direct and inverse materialization, including Header.Context.Container and the Project root. (ETA: 10–20 min per work unit.)
- [ ] Verify create, update, retarget and remove behavior through SQL and GRAPH_TABLE. (ETA: 10–20 min per work unit.)

## Acceptance

The tested consumer matches the accepted declarations; source issues and unsupported qualified derivations are explicitly resolved or held.
