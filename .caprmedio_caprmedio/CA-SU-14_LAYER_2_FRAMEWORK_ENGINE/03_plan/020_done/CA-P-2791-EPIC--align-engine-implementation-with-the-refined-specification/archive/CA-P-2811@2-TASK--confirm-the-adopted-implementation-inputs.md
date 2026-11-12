---
identity:
  id: CA-P-2811
  ref_id: CA-P-2811@2
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
  version: 2
  updated_at: 2026-11-09 21:20:12 +0400
destination:
  file:
    name: CA-P-2811@2-TASK--confirm-the-adopted-implementation-inputs.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/archive
author: Anatoly Maslennikov
---

## Summary

Confirm the adopted implementation inputs

## Objective

Review the next task, fix its inputs, and compile or reuse applicable Direct/Approach Policies from PROGRAMMATIC to its owning Scope. Gather only implemented RED and non-Policy M. Keep old Tools and the benchmark corpus out.

## Subtasks

- [ ] Review and fix the next scoped input batch. (ETA: up to 15 min.)
- [ ] Complete one scoped implementation or verification batch; split before exceeding 20 min.
- [ ] Review and fix the result; record a small P / Work Report. (ETA: up to 15 min.)

## Definition of Done

The stated work has actual source/code/test evidence. Every unresolved or unrun case is explicit; no Task text replaces RMED.

## Input refresh

P2767/P2840 source adoption is complete. Confirm Current replacement lineage from the thin summary-merges.tsv before using I7–I9 or module source pins. Keep six merge holds, the 69 prior MED hold and the benchmark excluded. Review query readability of concurrently adopted M514/M515 before compiling policies, including the latest model-declared lowercase Header values. Record any missing consumer support in the existing Backend/audit tasks; do not silently omit applicable policies.
