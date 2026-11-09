---
identity:
  id: CA-P-2839
  ref_id: CA-P-2839
context:
  container:
    atom: CA-P-2791
  role: Plan
  form: Plan
  label: Task
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 4
state:
  status: Backlog
  version: 1
  updated_at: 2026-11-09 15:49:38 +0400
destination:
  file:
    name: CA-P-2839-TASK--relocate-release-implementation-and-tests.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification
author: Anatoly Maslennikov
relations:
  IS_BLOCKED_BY:
  - CA-P-2837
  - CA-P-2811
---

## Summary

Relocate release implementation and tests

## Objective

Review and implement the adopted FRAMEWORK_DELIVERY specification for the complete local/public release families. Relocate their implementation and tests, update affected callers and verify the resulting release entry points. Keep generic Engine dependencies with their existing responsibilities.

## Subtasks

- [ ] Review the next implementation batch against Current RMEDO and applicable Method Policies. (ETA: up to 15 min.)
- [ ] Prepare and review the bounded relocation and caller changes. (ETA: up to 20 min per batch.)
- [ ] Apply each reviewed batch and run its relevant checks. (ETA: up to 20 min per batch.)
- [ ] Verify both release entry points and report remaining limitations. (ETA: up to 20 min.)

## Definition of Done

The affected implementation, tests, callers and delivery references agree with the adopted specification. Local/public release behavior and safety checks remain covered. Real publication or release requires its own authorized Run; this Task does not itself authorize either.
