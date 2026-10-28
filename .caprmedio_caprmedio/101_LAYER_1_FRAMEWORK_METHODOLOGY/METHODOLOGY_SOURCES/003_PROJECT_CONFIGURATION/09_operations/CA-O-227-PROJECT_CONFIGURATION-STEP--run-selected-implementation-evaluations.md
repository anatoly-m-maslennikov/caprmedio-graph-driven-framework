---
atom_id: CA-O-227
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Active
version: 11
updated_at: 2026-10-27 19:59:48 +0400
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Requirement'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Method'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Delivery'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification/Dynamic Testing
  - Subject/CAPRMEDIO/Carrier
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
relations: {}
tier: 3
---
# Summary

Run selected implementation Evaluations

## Operation

This Step invokes CA-O-020 in Integrated context with the exact candidate, selected checks/commands, current R/E/D and complete M bindings, Project Principles, complete test inputs and fixtures, permissions, execution phase, and retained issue and regression evidence. Bind the existing selected Plan, or bind the actual admitted in-session P/task with its instruction, Definition of Done, and source context. If CA-O-020's selected P/Plan input is not actually satisfied, return `blocked`; never invent a Plan Atom ID or weaken CA-O-020.

Retain actual output, failed/blocked/unevaluated/stale results and candidate bindings. Return CA-O-020's `passed`, `failed`, or `blocked` result unchanged. No diagnosis, edit, expectation change, retry, or repair.

## Details

`blocked` is terminal unresolved with evidence retained; `passed` and `failed` route through the Workflow's explicit transitions.
