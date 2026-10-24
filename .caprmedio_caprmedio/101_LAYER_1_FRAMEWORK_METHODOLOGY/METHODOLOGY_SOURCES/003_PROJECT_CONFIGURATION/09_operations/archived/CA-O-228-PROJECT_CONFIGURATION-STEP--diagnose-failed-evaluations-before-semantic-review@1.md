---
atom_id: "CA-O-228"
content_role: "Operations"
type: "Step"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
author: "Anatoly Maslennikov"
status: "Active"
version: 1
updated_at: "2026-10-21T22:49:16Z"
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
    - "CA-O-089"
    - "CA-O-020"
    - "CA-M-390"
    - "CA-M-396"
    - "CA-M-397"
    - "CA-M-398"
---
# Summary

Diagnose failed Evaluations before semantic review

## Operation

This Step invokes CA-O-089 in Isolated context with the exact candidate, failed output, selected existing Plan or actual admitted in-session P/task including instruction/Definition of Done/source context, prepared checks, phase, R/E/D and M bindings, relevant inputs, confidence/permission gates, and report/run bindings. CA-O-089's input and semantics remain unchanged.

Retain and pass its six possible results unchanged: `expected_initial_failure`, `implementation_defect`, `test_implementation_defect`, `authority_change_required`, `environment_blocker`, and `unresolved`. Do not edit code, tests, expected behavior, Atoms, or status.

## Details

No hidden retry or repair route and no unsupported subagent promise. The Workflow's semantic Step applies the explicit result mapping and retains failed checks, findings, blockers, and uncertainty.
