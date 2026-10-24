---
atom_id: CA-O-227
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Active
version: 7
updated_at: 2026-10-24 01:18:03 +0400
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step'
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Requirement'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Method'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Evaluation'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Delivery'
  - Subject/Engineering/Implementation Evaluation
  - Subject/Engineering/Carrier
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Domain/Node/Occurrent/Execution/Step Run
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
relations:
  relates_to:
  - CA-O-223
  - CA-O-020
  - CA-O-016
  - CA-M-424
  - CA-M-395
  - CA-E-389
  - CA-E-539
  - CA-E-540
tier: 3
---
# Summary

Run selected implementation Evaluations

## Operation

This Step invokes CA-O-020 in Integrated context with the exact candidate, selected checks/commands, current R/E/D and complete M bindings, Project Principles, complete test inputs and fixtures, permissions, execution phase, and retained issue and regression evidence. Bind the existing selected Plan, or bind the actual admitted in-session P/task with its instruction, Definition of Done, and source context. If CA-O-020's selected P/Plan input is not actually satisfied, return `blocked`; never invent a Plan Atom ID or weaken CA-O-020.

Retain actual output, failed/blocked/unevaluated/stale results and candidate bindings. Return CA-O-020's `passed`, `failed`, or `blocked` result unchanged. No diagnosis, edit, expectation change, retry, or repair.

## Details

`blocked` is terminal unresolved with evidence retained; `passed` and `failed` route through the Workflow's explicit transitions.
