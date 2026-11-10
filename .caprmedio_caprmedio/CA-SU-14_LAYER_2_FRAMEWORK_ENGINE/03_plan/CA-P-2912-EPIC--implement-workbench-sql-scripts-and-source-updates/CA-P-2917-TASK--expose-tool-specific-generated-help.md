---
identity:
  id: CA-P-2917
  ref_id: CA-P-2917
context:
  container:
    atom: CA-P-2912
  role: Plan
  form: Plan
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 4
  label: Task
state:
  status: Backlog
  version: 1
  updated_at: 2026-11-11 00:51:59 +0400
destination:
  file:
    name: CA-P-2917-TASK--expose-tool-specific-generated-help.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2912-EPIC--implement-workbench-sql-scripts-and-source-updates
author: Anatoly Maslennikov
relations:
  IS_BLOCKED_BY:
  - CA-P-2913
---

## Summary

Expose tool-specific generated help

## Objective

Implement Current R970308647, M548 and D714; verify E820 through the actual MCP boundary. Reuse the generated registry and existing Project/exclusion behavior.

## Subtasks

- [ ] Review and fix the next bounded input batch. (ETA: up to 15 min.)
- [ ] Implement or verify one scoped batch; split before 20 min.
- [ ] Independently review, fix and record actual results. (ETA: up to 15 min.)

## Definition of Done

Actual implementation and acceptance evidence covers the admitted batch; record unresolved and unrun cases. Tasks do not replace RMEDO.
