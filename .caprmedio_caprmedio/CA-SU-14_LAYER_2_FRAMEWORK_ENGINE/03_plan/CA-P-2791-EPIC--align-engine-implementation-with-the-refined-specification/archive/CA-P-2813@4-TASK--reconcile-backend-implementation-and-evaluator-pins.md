---
identity:
  id: CA-P-2813
  ref_id: CA-P-2813@4
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
  version: 4
  updated_at: 2026-11-11 04:39:44 +0400
destination:
  file:
    name: CA-P-2813@4-TASK--reconcile-backend-implementation-and-evaluator-pins.md
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

- [ ] Review and fix the next scoped input batch. (ETA: up to 15 min.)
- [ ] Complete one scoped implementation or verification batch; split before exceeding 20 min.
- [ ] Review and fix the result; record a small P / Work Report. (ETA: up to 15 min.)

## Definition of Done

The stated work has actual source/code/test evidence. Every unresolved or unrun case is explicit; no Task text replaces RMED.


## Verified watcher batch

C712 is Resolved after the retained mixed real-project canary passed against the running image without reread. Full Atom and Scope Declaration canaries also passed with mutation-to-query timers and exact image/version attribution. P2925 records this bounded acceptance. This Task remains Active: complete Backend contract/pin reconciliation and resolve C729/P2866 model admission before final acceptance.


## Current contract review

Do not mass-bump historical module pins. Compare each implemented Claim portion against its Current source and verified behavior. R2723@4 and @5 have identical Markdown content; verify and reconcile the source-row pin narrowly. Keep schema/compiler pin changes pending P2866 and the CA #5 source clarification.

D673@18 requires ordered column metadata from Check. The existing Check path has that metadata but drops it from the response. Correct the shared owner and verify exact types, duplicate aliases, zero-row metadata and temporary-result cleanup without query rows, SQL echo, exports, save or log effects. Then verify the actual adapters. This is implementation of the adopted delivery contract, not a new query capability.
