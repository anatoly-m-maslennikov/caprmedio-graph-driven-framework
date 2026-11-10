---
identity:
  id: CA-P-2906
  ref_id: CA-P-2906
context:
  container:
    scope_unit: CA-SU-00
  role: Plan
  form: Plan
  label: Task
  topics:
    main_subject: MODEL//CAPRMEDIO <+ Atom
  tier: 4
state:
  status: Done
  version: 1
  updated_at: 2026-11-11 00:22:28 +0400
destination:
  file:
    name: CA-P-2906-TASK--align-workflow-rmedo-with-sql-scripts-and-atom-lifecycle.md
    path: .caprmedio_caprmedio/03_plan
author: Anatoly Maslennikov
---

## Summary

Align Workflow RMEDO with SQL scripts and Atom lifecycle

## Objective

Reconcile the native Workflow, Step, lifecycle, Workbench and MCP help source contracts with the Operator's latest decisions. Keep implementation and deployment separate from source adoption.

## Scope

Core Workflow and Step declarations and their direct Method/Evaluation/Delivery contracts; Current and WIP Atom lifecycle operations and directly affected evaluations; Workbench Tab scripts, source-backed SQL updates, Draft and in-place modes, queryable issue discovery; shared MCP help contracts. Keep the four proposed specification-work workflows as WIP Drafts. Preserve unrelated concurrent work and historical or generated copies.

## Completion criteria

The affected native source contracts agree, actual file locations and identities remain consistent, independent review findings are fixed, and the exact Current source handoff is available to the implementation Epic. Document unresolved questions and the boundary between adopted contracts, WIP definitions and runtime behavior.
