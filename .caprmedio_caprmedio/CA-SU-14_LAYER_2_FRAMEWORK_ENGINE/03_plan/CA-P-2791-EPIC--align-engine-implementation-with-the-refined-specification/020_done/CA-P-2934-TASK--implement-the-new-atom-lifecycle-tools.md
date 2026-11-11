---
identity:
  id: CA-P-2934
  ref_id: CA-P-2934
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
  status: done
  version: 7
  updated_at: '2026-11-11T21:52:12.066178+04:00'
destination:
  file:
    name: CA-P-2934-TASK--implement-the-new-atom-lifecycle-tools.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done
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

- [x] Review the Atom Lifecycle Workflow and adapter contracts. Fix gaps in RMEDO before implementation. (ETA: up to 15 min.)
- [x] Gather the applicable Method Policies and scoped implementation inputs. (ETA: up to 15 min.)
- [x] Implement and register the new Tools using the existing adapters. Split into batches of up to 20 min.
- [x] Verify the admitted lifecycle operations through the real Tool interface using a disposable Project. Split checks into batches of up to 20 min.
- [x] Review and fix the result; record a short Work Report. (ETA: up to 15 min.)

## Definition of Done

The admitted Atom Lifecycle Workflows are available as new Tools, use the existing adapters, and pass their real-interface Evaluations. Retired Tools and the generic Workflow engine stay deferred.


## Contract review

The Operator deferred formal Scope Delegation admission to version 0.7. CA-P-3000 tracks the redesign of allowed Roles, Forms, and Subjects. This Task continues to track lifecycle Tool delivery and verification.

The selected Workflow definitions and their supporting Atoms are Current. CA-P-2976 records the adopted sources and adapter checks. CA-C-730 tracks the remaining Tool implementation and real-interface checks.

## Delivery

All six lifecycle Tools are registered on the live Project MCP endpoint. The exact-image disposable Project verified all six, including parent-first reopening under the Operator’s decision. The resource guard passed on an isolated rerun. CA-P-3001 records the acceptance evidence. The Methodology handoff for CA-O-10011 is tracked in CA-C-730.

The Current CA-O-10011 Workflow now records parent-first reopening. CA-P-3002 records the final release and lifecycle verification.
