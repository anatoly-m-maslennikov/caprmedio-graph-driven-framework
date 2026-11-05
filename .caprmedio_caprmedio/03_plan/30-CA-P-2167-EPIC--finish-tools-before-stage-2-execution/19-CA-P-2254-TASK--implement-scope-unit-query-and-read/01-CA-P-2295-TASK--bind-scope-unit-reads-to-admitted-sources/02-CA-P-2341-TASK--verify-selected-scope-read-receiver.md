---
atom_id: CA-P-2341
ref_id: CA-P-2341
role: Plan
form: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
topics:
  main_subject: Subject/Graph Node/Engineering/Continuant/Tool
  dependencies:
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Node/Engineering/Project Structure Declaration
  - Subject/Graph Node/Engineering/Project Settings Snapshot
  - Subject/Graph Node/Engineering/Scope Unit Declaration Read Adapter Construction
  - Subject/Graph Node/Engineering/Workflow
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
version: 9
updated_at: 2026-10-25 17:32:27 +0400
relations:
  is_decomposition_of:
  - CA-P-2295
tier: 3
container:
  atom: CA-P-2295
carrier_destination:
  file:
    name: 2-CA-P-2341-TASK--verify-selected-scope-read-receiver.md
    path: .caprmedio_caprmedio/03_plan/30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/19-CA-P-2254-TASK--implement-scope-unit-query-and-read/1-CA-P-2295-TASK--bind-scope-unit-reads-to-admitted-sources
---
# Summary

Verify selected Scope Read receiver

## Objective

Independent tests prove the production Scope Read receiver executes through genuine admission and preserves source bytes.

## Details

### Current continuation checkpoint — 2026-10-13 22:13:02 +0400

Independent receiving verification passed 12 actual Session checks, including current source copies, full Structure output, stale/missing/wrong Action evidence, denied permission, mutation refusal and unchanged source/Journal bytes. Root integration passed all 264 connector tests. Evidence is selected-read-receivers-checkpoint.md under the tools-first projection. Disposable complete Settings schemas in fixtures do not prove production Settings policy. Keep this verification Task Active for the eventual accepted production reader binding; no live/runtime route acceptance is implied.

Estimated own work: up to 15 minutes. Split before exceeding this bound. Root owns Plans and Git; workers own disjoint implementation/test files and preserve other workers' edits. Inherit accepted parent RMEDO and independent review gates.

Prepare independent complete root/child outputs and stale/denied/wrong-action/context/project/schema/missing/ambiguous cases. Use real RunExecutionSession and selected Action authority; do not mock SelectedOperationAdmission.check or create synthetic logical Settings Revision evidence. Final acceptance waits for P2340 frozen code. Prove effects=[] for targets; genuine Run/Journal recording is distinct from target effects. No installed activation or live source changes.

### Definition of Done

The outcome has exact current source/code/test evidence, actual positive/refusal checks and independent acceptance. Preparation, isolated helpers or source acceptance do not establish live/runtime completion. No unapproved policy, weakened guard, live Core migration or deferred capability is included.
