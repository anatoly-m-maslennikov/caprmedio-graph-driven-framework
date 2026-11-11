---
identity:
  id: CA-P-2934
  ref_id: CA-P-2934@5
context:
  container:
    atom: CA-P-2791
  role: Plan
  form: Plan
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 4
  label: Task
state:
  status: Archived
  version: 5
  updated_at: 2026-11-11 20:34:11 +0400
destination:
  file:
    name: CA-P-2934@5-TASK--implement-the-new-atom-lifecycle-tools.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/099_archived
author: Anatoly Maslennikov
relations:
  IS_BLOCKED_BY:
  - CA-P-2811
---

## Summary

Implement the new Atom Lifecycle Tools

## Objective

Implement the admitted Atom Lifecycle Workflows as new Tools using the existing adapters. Use Current RMEDO as the specification; review any required Drafts before adoption or implementation.

## Subtasks

- [ ] Review the Atom Lifecycle Workflow and adapter contracts. Fix gaps in RMEDO before implementation. (ETA: up to 15 min.)
- [x] Gather the applicable Method Policies and scoped implementation inputs. (ETA: up to 15 min.)
- [ ] Implement and register the new Tools using the existing adapters. Split into batches of up to 20 min.
- [ ] Verify the admitted lifecycle operations through the real Tool interface using a disposable Project. Split checks into batches of up to 20 min.
- [ ] Review and fix the result; record a short Work Report. (ETA: up to 15 min.)

## Definition of Done

The admitted Atom Lifecycle Workflows are available as new Tools, use the existing adapters, and pass their real-interface Evaluations. Retired Tools and the generic Workflow engine stay deferred.


## Contract review

The Operator deferred formal Scope Delegation admission to version 0.7. CA-P-3000 tracks the redesign of allowed Roles, Forms, and Subjects. This Task continues to track lifecycle Tool delivery and verification.

The selected Workflow definitions and their supporting Atoms are Current. CA-P-2976 records the adopted sources and adapter checks. CA-C-730 tracks the remaining Tool implementation and real-interface checks.
