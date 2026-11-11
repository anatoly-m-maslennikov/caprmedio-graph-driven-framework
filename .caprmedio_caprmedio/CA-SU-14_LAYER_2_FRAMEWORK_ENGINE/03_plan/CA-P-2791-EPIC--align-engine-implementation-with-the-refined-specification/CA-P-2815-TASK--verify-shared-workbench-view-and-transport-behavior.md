---
identity:
  id: CA-P-2815
  ref_id: CA-P-2815
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
  version: 5
  updated_at: 2026-11-11 07:44:19 +0400
destination:
  file:
    name: CA-P-2815-TASK--verify-shared-workbench-view-and-transport-behavior.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification
author: Anatoly Maslennikov
relations:
  IS_BLOCKED_BY:
  - CA-P-2811
---

## Summary

Verify shared Workbench View and transport behavior

## Objective

Exercise adopted View operations, result lifetime, schema naming, formatting, grid behavior and shared HTTP/MCP effects. Measure the Compact target. Keep real native Codex rendering and standalone-chat work deferred; do not count skipped cases as passes.

## Subtasks

- [x] Confirm Current editor/display/transport acceptance and exclusive file ownership. (ETA: up to 15 min.)
- [x] Verify one editor or View/Tab operation batch through the actual browser interface. Split before 20 min.
- [x] Verify one theme, zoom or grid batch with the applicable Evaluations. Split before 20 min.
- [x] Measure Compact at equivalent viewport/zoom against the recovered historical baseline; report a missing baseline explicitly. (ETA: up to 20 min.)
- [x] Verify shared HTTP/MCP outcomes in a separate transport batch after Backend changes. Split before 20 min.
- [x] Independently review/fix each result and record a small Work Report. (ETA: up to 15 min.)

## Definition of Done

The stated work has actual source/code/test evidence. Every unresolved or unrun case is explicit; no Task text replaces RMED.


## Verified batches

P2926 records nine passing real-image View/grid browser tests and eight shared HTTP/MCP Workspace E2E tests, including E819. P2924 records completion acceptance; P2925 records real native-watcher canaries. The Task remains Active until the complete adopted View/result-lifetime/display checklist is reconciled. The recovered Compact comparison meets the half-height target against its historical proxy; the exact screenshot build/zoom is unverified. No native Codex rendering or standalone-chat acceptance is added.

## Verified acceptance

P2943, P2947 and P2954 record the browser and adapter checks. The rebuilt image passed browser, shared grid and result-lifetime tests. The Compact proxy is recorded with its historical baseline limitation. Native Codex rendering and standalone chat remain deferred.
