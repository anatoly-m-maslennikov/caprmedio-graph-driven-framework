---
identity:
  atom_id: CA-P-3006
  ref_id: CA-P-3006
context:
  container:
    atom: CA-P-2791
  role: plan
  form: plan
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 4
  label: Task
state:
  status: done
  version: 1
  updated_at: '2026-11-11T23:40:04.931365+04:00'
destination:
  file:
    name: CA-P-3006-TASK--fix-live-atom-lifecycle-latency-and-scope-unit-refresh.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/020_done/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done
relations:
  IS_BLOCKED_BY:
  - CA-P-2934
author: Anatoly Maslennikov
---

## Summary

Fix live Atom lifecycle latency and Scope Unit refresh

## Objective

- Make lifecycle writes accept new Scope Units without an MCP restart.
- Remove redundant filesystem work that caused the live Update call to exceed 180 seconds.
- Rerun the seeded live lifecycle checks and record MCP response times, Workbench visibility, and fixture cleanup.
