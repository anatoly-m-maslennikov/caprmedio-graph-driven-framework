---
identity:
  id: CA-P-2724
  ref_id: CA-P-2724@3
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
  status: Archived
  version: 3
  updated_at: 2026-11-08 20:22:21 +0400
destination:
  file:
    name: 09-CA-P-2724@3-TASK--prepare-drafts-for-workbench-and-its-descendants.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes/archived
author: Anatoly Maslennikov
relations:
  IS_BLOCKED_BY:
  - CA-P-2716
  - CA-P-2736
---

## Summary

Prepare Drafts for WORKBENCH and its descendants

## Objective

Every in-scope Current RMEDO Atom is accounted for by a Draft or explicit held disposition; no existing Draft or Archive is migrated silently.

## Working procedure

Before starting or continuing a Task or subtask, review its next work unit and fix missing inputs or acceptance criteria first. If confidence is below 90%, re-read the Operator input. If still below 90%, ask the Operator and continue independent unblocked work.

Keep one small P / Work Report per Task and update it during execution. Until the shared Work Report model is adopted, reports are explicitly provisional and do not claim model or runtime adoption.

## Details

Subtasks below are work units, each with an estimated 10–20 minutes. Split a larger unit before starting it. For Atom batches, select a small number that fits the time box and repeat by batch; do not treat the whole inventory as one subtask. Assign at most one Scope Unit to each worker. Terra and Luna may handle bounded work; main judgments and final review use GPT-6.1 Sol at High effort.

## Draft ownership

Use the owner recorded by CA-P-2716 for each Atom. Only that owner writes its Draft; overlapping inventories link to that Draft. A worker owns one Scope Unit at a time.

## Subtasks

- [ ] Inventory Current RMEDO separately for WORKBENCH and each declared descendant. (ETA: 10–20 min per work unit.)
- [ ] Create Drafts in small batches, with one owning Scope Unit per worker. (ETA: 10–20 min per work unit.)
- [ ] Account separately for performance-canary data and report any uncertain inclusion before rewriting it. (ETA: 10–20 min per work unit.)

## Acceptance

Every in-scope Current RMEDO Atom is accounted for by a Draft or explicit held disposition; no existing Draft or Archive is migrated silently.
