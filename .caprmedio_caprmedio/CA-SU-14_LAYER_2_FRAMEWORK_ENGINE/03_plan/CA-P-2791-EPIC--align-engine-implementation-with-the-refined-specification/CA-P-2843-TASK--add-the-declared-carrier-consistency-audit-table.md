---
identity:
  id: CA-P-2843
  ref_id: CA-P-2843
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
  status: Done
  version: 3
  updated_at: 2026-11-11 06:40:07 +0400
destination:
  file:
    name: CA-P-2843-TASK--add-the-declared-carrier-consistency-audit-table.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification
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

- [x] Create or update the related RMED; review and fix it. (ETA: up to 20 min per batch.)
- [x] Gather applicable Method Policies and implement the accepted RMED. (ETA: up to 20 min per batch.)
- [x] Add E2E coverage, review and fix the result, and record a small Work Report. (ETA: up to 20 min per batch.)

## Definition of Done

The accepted RMED defines the table and its checks. Query-visible results identify the actual affected sources; E2E evidence covers both positive and negative cases. This Task does not replace the specification or authorize automatic source repair.

## Adopted inputs

The reviewed audit contracts R970308648–R970308650, M549, D715 and E821 are Current at version 1. Use the exact source paths and hashes in `audits/adoption.json` under this Epic's implementation packet. Their Claims hold table semantics; this Task only tracks implementation and acceptance.
