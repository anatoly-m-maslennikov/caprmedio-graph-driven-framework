---
identity:
  id: CA-P-2860
  ref_id: CA-P-2860@2
context:
  container:
    scope_unit: CA-SU-14
  role: Plan
  form: Plan
  label: Task
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 4
state:
  status: Archived
  version: 2
  updated_at: 2026-11-11 00:29:06 +0400
destination:
  file:
    name: CA-P-2860@2-TASK--implement-session-bound-workflow-run-reads.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/backlog/archive
relations:
  IS_BLOCKED_BY:
  - CA-P-2811
  - CA-P-2858
---

## Summary

Implement session-bound Workflow Run reads

## Objective

Implement the adopted session envelope and per-session active Run/history RMEDO. Gather applicable Method Policies first. Test the shared gateway and backend with two sessions and two Projects; preserve native Tool arguments. Do not restore retired workflow tools wholesale.

## Subtasks

- [ ] Review the next scoped inputs and fix gaps. (ETA: up to 15 min.)
- [ ] Complete one scoped batch; split before 20 minutes.
- [ ] Review the result and write a small Work Report. (ETA: up to 15 min.)

## Definition of Done

The scoped deliverable is reviewed and its actual checks and remaining holds are recorded. Tasks do not replace RMEDO.

## Deferral

The Operator deferred Run/history reads on 11 November 2026. Generic session context and the plugin-free hook proceed in P2910/P2861. Do not add a parallel Run store or return empty success for an absent state owner.
