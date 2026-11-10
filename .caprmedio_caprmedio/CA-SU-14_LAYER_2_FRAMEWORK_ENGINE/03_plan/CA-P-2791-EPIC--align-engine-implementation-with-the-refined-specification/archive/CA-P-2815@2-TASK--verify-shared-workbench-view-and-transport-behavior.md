---
identity:
  id: CA-P-2815
  ref_id: CA-P-2815@2
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
  updated_at: 2026-11-11 00:15:31 +0400
destination:
  file:
    name: CA-P-2815@2-TASK--verify-shared-workbench-view-and-transport-behavior.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/archive
author: Anatoly Maslennikov
relations:
  IS_BLOCKED_BY:
  - CA-P-2811
  - CA-P-2812
---

## Summary

Verify shared Workbench View and transport behavior

## Objective

Exercise adopted View operations, result lifetime, schema naming, formatting, grid behavior and shared HTTP/MCP effects. Measure the Compact target. Keep real native Codex rendering and standalone-chat work deferred; do not count skipped cases as passes.

## Subtasks

- [ ] Confirm Current editor/display/transport acceptance and exclusive file ownership. (ETA: up to 15 min.)
- [ ] Verify one editor or View/Tab operation batch through the actual browser interface. Split before 20 min.
- [ ] Verify one theme, zoom or grid batch with the applicable Evaluations. Split before 20 min.
- [ ] Measure Compact at equivalent viewport/zoom against the recovered historical baseline; report a missing baseline explicitly. (ETA: up to 20 min.)
- [ ] Verify shared HTTP/MCP outcomes in a separate transport batch after Backend changes. Split before 20 min.
- [ ] Independently review/fix each result and record a small Work Report. (ETA: up to 15 min.)

## Definition of Done

The stated work has actual source/code/test evidence. Every unresolved or unrun case is explicit; no Task text replaces RMED.
