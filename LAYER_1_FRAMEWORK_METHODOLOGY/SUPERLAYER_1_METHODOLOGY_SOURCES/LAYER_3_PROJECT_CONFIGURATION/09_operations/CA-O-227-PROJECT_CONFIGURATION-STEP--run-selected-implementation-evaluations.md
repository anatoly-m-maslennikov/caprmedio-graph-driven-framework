---
atom_id: "CA-O-227"
content_role: "Operations"
type: "Step"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
author: "Anatoly Maslennikov"
status: "Active"
version: 3
updated_at: "2026-10-21T23:29:13+00:00"
global_tier: 11
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Step"
  depends_on:
    - "Entity/Node/Continuant/Atom/Content Role: Requirement"
    - "Entity/Node/Continuant/Atom/Content Role: Method"
    - "Entity/Node/Continuant/Atom/Content Role: Evaluation"
    - "Entity/Node/Continuant/Atom/Content Role: Delivery"
    - "Entity/Node/Continuant/Implementation"
    - "Entity/Carrier"
    - "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action"
    - "Entity/Node/Occurrent/Execution/Step Run"
    - "Entity/Node/Occurrent/Execution/Workflow Run"
relations:
  relates_to:
    - "CA-O-223"
    - "CA-O-020"
    - "CA-O-016"
    - "CA-M-424"
    - "CA-M-395"
    - "CA-E-389"
    - "CA-E-539"
    - "CA-E-540"
---
# Summary

Run selected implementation Evaluations

## Operation

This Step invokes CA-O-020 in Integrated context with the exact candidate, selected checks/commands, current R/E/D and complete M bindings, Project Principles, complete test inputs and fixtures, permissions, execution phase, and retained issue and regression evidence. Bind the existing selected Plan, or bind the actual admitted in-session P/task with its instruction, Definition of Done, and source context. If CA-O-020's selected P/Plan input is not actually satisfied, return `blocked`; never invent a Plan Atom ID or weaken CA-O-020.

Retain actual output, failed/blocked/unevaluated/stale results and candidate bindings. Return CA-O-020's `passed`, `failed`, or `blocked` result unchanged. No diagnosis, edit, expectation change, retry, or repair.

## Details

`blocked` is terminal unresolved with evidence retained; `passed` and `failed` route through the Workflow's explicit transitions.
