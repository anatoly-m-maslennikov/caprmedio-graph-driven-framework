---
identity:
  id: CA-P-2910
  ref_id: CA-P-2910
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
  version: 2
  updated_at: 2026-11-11 00:58:51 +0400
destination:
  file:
    name: CA-P-2910-TASK--implement-generic-runtime-session-context.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done
author: Anatoly Maslennikov
relations:
  IS_BLOCKED_BY:
  - CA-P-2811
  - CA-P-2814
---

## Summary

Implement generic runtime session context

## Objective

Implement the approved generic runtime context and MCP envelope from Current M517; verify the receiving boundary through E814 before enabling the standalone hook. Run/history reads remain deferred.

## Subtasks

- [ ] Review Current inputs and applicable Method Policies; assign separate PROGRAMMATIC-local and MCP ownership. (ETA: up to 15 min.)
- [ ] Implement and verify task-local runtime binding. Split before 20 min.
- [ ] Implement and verify the public MCP envelope and native-argument preservation. Split before 20 min.
- [ ] Review and fix the combined result through real MCP boundary cases. (ETA: up to 20 min.)

## Definition of Done

The accepted context contract works across the actual gateway with isolated sessions and preserved native arguments. Report hook activation separately; do not claim Workflow Run reads or invent a state owner.
