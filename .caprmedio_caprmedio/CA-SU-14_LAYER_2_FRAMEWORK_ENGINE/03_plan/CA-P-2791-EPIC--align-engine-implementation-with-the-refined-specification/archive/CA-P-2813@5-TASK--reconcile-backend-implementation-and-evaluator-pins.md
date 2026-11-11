---
identity:
  id: CA-P-2813
  ref_id: CA-P-2813@5
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
  updated_at: 2026-11-11 07:51:17 +0400
destination:
  file:
    name: CA-P-2813@5-TASK--reconcile-backend-implementation-and-evaluator-pins.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/archive
author: Anatoly Maslennikov
relations:
  IS_BLOCKED_BY:
  - CA-P-2811
---

## Summary

Reconcile Backend implementation and evaluator pins

## Objective

Review I7 and the thin implementation map. Compare each adopted Backend contract against its implementing module and evaluator. Correct only actual mismatches; retain package-time versus runtime schema separation. Do not mass-bump pins or pin called dependencies.

## Subtasks

- [x] Review and fix the next scoped input batch. (ETA: up to 15 min.)
- [x] Complete one scoped implementation or verification batch; split before exceeding 20 min.
- [x] Review and fix the result; record a small P / Work Report. (ETA: up to 15 min.)

## Definition of Done

The stated work has actual source/code/test evidence. Every unresolved or unrun case is explicit; no Task text replaces RMED.


## Verified watcher batch

C712 is Resolved after the retained mixed real-project canary passed against the running image without reread. Full Atom and Scope Declaration canaries also passed with mutation-to-query timers and exact image/version attribution. P2925 records this bounded acceptance. This Task remains Active: complete Backend contract/pin reconciliation and resolve C729/P2866 model admission before final acceptance.


## Current contract review

P2940 and P2949 verified ordered Check metadata and the shared query behavior. P2952 verified schema generation and loading across two real image builds. P2955 records the final Current references for the six affected modules. Only the versioned reference comments differ from the tested image.

Confirm the released Workbench reads the Current model and exposes the declared Content columns and compiled relations. Close C729 with that evidence.
