---
identity:
  id: CA-P-2912
  ref_id: CA-P-2912
context:
  container:
    scope_unit: CA-SU-14
  role: Plan
  form: Plan
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 3
  label: Epic
state:
  status: Backlog
  version: 3
  updated_at: 2026-11-11 02:04:04 +0400
destination:
  file:
    name: CA-P-2912-EPIC--implement-workbench-sql-scripts-and-source-updates.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan
author: Anatoly Maslennikov
relations:
  IS_BLOCKED_BY:
  - CA-P-2791
---

## Summary

Implement Workbench SQL scripts and source updates

## Objective

Review and adopt the proposed SQL capabilities, then implement them after completing P2791.

## Scope

All Workflow-engine work is deferred by the Operator. This follow-up does not introduce or restore an executor, scheduler, orchestration, routing, Run-state/history or recovery service.

The Operator assigned these new capabilities to a follow-up Epic on 11 November 2026. The Operator returned the SQL UPDATE contracts to Draft. The earlier source handoff is historical for these seven proposals. Review and adopt the Drafts below before implementation; refresh the Current source set, versions and hashes before dispatch. SQL scripts, source-backed updates and their Tab/help integration are pending implementation, not P2791 acceptance. Run/history reads, native Codex rendering, standalone chat and retired Tool routes retain their separate deferrals.

## Procedure

Draft RMEDO → review/fix → adoption → Current RMEDO → applicable Method Policy prompt → REDO plus non-Policy M → bounded implementation → actual E2E → independent review/fix. One receiving Scope Unit per worker, exclusive paths and batches of at most 15–20 minutes.

## SQL proposal Drafts

- CA-R-2727@21-draft
- CA-R-2728@9-draft
- CA-M-550@1-draft
- CA-D-673@19-draft
- CA-D-674@27-draft
- CA-O-242@1-draft
- CA-E-822@1-draft

## Tasks

- [ ] [Confirm the adopted SQL implementation inputs](CA-P-2912-EPIC--implement-workbench-sql-scripts-and-source-updates/CA-P-2913-TASK--confirm-the-adopted-sql-implementation-inputs.md)
- [ ] [Implement sequential SQL scripts](CA-P-2912-EPIC--implement-workbench-sql-scripts-and-source-updates/CA-P-2914-TASK--implement-sequential-sql-scripts.md)
- [ ] [Implement source-backed SQL updates](CA-P-2912-EPIC--implement-workbench-sql-scripts-and-source-updates/CA-P-2915-TASK--implement-source-backed-sql-updates.md)
- [ ] [Align Tabs with script execution](CA-P-2912-EPIC--implement-workbench-sql-scripts-and-source-updates/CA-P-2916-TASK--align-tabs-with-script-execution.md)
- [ ] [Expose tool-specific generated help](CA-P-2912-EPIC--implement-workbench-sql-scripts-and-source-updates/CA-P-2917-TASK--expose-tool-specific-generated-help.md)
- [ ] [Verify and deliver source-backed query changes](CA-P-2912-EPIC--implement-workbench-sql-scripts-and-source-updates/CA-P-2918-TASK--verify-and-deliver-source-backed-query-changes.md)

## Definition of Done

The accepted in-scope source contracts are implemented and verified through actual interfaces and lifecycle cases without regressing performance or resource limits. Report delivery separately.
