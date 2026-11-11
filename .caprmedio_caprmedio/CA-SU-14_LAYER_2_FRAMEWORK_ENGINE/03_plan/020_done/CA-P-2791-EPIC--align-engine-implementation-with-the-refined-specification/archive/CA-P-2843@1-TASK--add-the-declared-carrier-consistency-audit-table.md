---
identity:
  id: CA-P-2843
  ref_id: CA-P-2843@1
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
  version: 1
  updated_at: 2026-11-09 19:08:55 +0400
destination:
  file:
    name: CA-P-2843@1-TASK--add-the-declared-carrier-consistency-audit-table.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/archive
author: Anatoly Maslennikov
relations:
  IS_BLOCKED_BY:
  - CA-P-2811
---

## Summary

Add the declared carrier consistency audit table

## Objective

Create and review RMED for a table listing Atoms whose declared file.name or file.path conflicts with their other properties. Then implement and test it against consistent and conflicting declarations.

## Subtasks

- [ ] Create or update the related RMED; review and fix it. (ETA: up to 20 min per batch.)
- [ ] Gather applicable Method Policies and implement the accepted RMED. (ETA: up to 20 min per batch.)
- [ ] Add E2E coverage, review and fix the result, and record a small Work Report. (ETA: up to 20 min per batch.)

## Definition of Done

The accepted RMED defines the table and its checks. Query-visible results identify the actual affected sources; E2E evidence covers both positive and negative cases. This Task does not replace the specification or authorize automatic source repair.
