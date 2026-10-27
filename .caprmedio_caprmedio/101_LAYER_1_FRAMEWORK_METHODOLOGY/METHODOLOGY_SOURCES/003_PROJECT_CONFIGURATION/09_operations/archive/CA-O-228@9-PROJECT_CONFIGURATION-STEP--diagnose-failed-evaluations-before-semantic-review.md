---
atom_id: CA-O-228@9
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Archived
version: 9
updated_at: 2026-10-26 05:59:45 +0400
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Requirement'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Method'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Evaluation'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Delivery'
  - Subject/Graph Node/Engineering/Implementation Failure Diagnosis
  - Subject/Graph Node/Engineering/Continuant/Carrier
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Domain/Occurrent/Execution/Step Run
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
relations: {}
tier: 3
---
# Summary

Diagnose failed Evaluations before semantic review

## Operation

This Step invokes CA-O-089 in Isolated context with the exact candidate, failed output, selected existing Plan or actual admitted in-session P/task including instruction/Definition of Done/source context, complete prepared tests/checks, phase, R/E/D and M bindings, relevant inputs, confidence/permission gates, and report/run bindings. CA-O-089's input and semantics remain unchanged.

Retain and pass its six possible results unchanged: `expected_initial_failure`, `implementation_defect`, `test_implementation_defect`, `authority_change_required`, `environment_blocker`, and `unresolved`. Do not edit code, tests, expected behavior, Atoms, or status.

## Details

No hidden retry or repair route and no unsupported subagent promise. The Workflow's semantic Step applies the explicit result mapping and retains failed checks, findings, blockers, and uncertainty.
