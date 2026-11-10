---
atom_id: CA-M-302
ref_id: CA-M-302
container:
  scope_unit: CA-SU-20
role: Method
form: Solution
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation/Code/Tool//WORKFLOW_ORCHESTRATOR
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Component
    Structure
tier: 4
relations:
  method_for:
  - CA-R-1605
  - CA-R-1523
  - CA-R-1524
status: Archived
version: 16
updated_at: 2026-11-09 19:30:15 +0400
cce_version: cce_1
cce_form: method
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
carrier_destination:
  file:
    name: CA-M-302@16-APPS-SOLUTION--separate-workflow-coordination-from-action-execution.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/05_method/archive
current_scope_unit: APPS
destination:
  file:
    name: CA-M-302-WORKFLOW_ORCHESTRATOR-SOLUTION--separate-workflow-coordination-from-action-execution.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-2_APP_WORKFLOW_ORCHESTRATOR/05_method
---

## Summary

Separate Workflow coordination from Action execution

## Claim

### Prose Claim

**to** implement WORKFLOW_ORCHESTRATOR, separate responsive coordination from long-running Action execution.

- use an on-demand local background service for coordination. an HTTP server, remote deployment, **or** graphical interface is **not** required by this Method.
- execute long-running **or** blocking Actions through bounded workers **or** subprocesses; waiting for external results **or** Operator input **must not** block the coordination interface.
- keep Workflow selection, transition, handoff, retry, **and** approval behavior driven by applicable methodology inputs rather than independently authored application branches.
- use stable request, Run, **and** dispatch identities with durable handoff recording, duplicate suppression, **and** the declared effect-safety mechanism. separate transient worker state from canonical Journal history **and** rebuildable views.
- keep client transport **and** worker adapters replaceable. select concrete libraries, wire formats, persistence Carriers, **and** resource limits through their applicable authority rather than assuming an unapproved default.

asynchronous coordination does **not** require **every** Action implementation **to** use asynchronous programming **or** execute concurrently. this Method does **not** install hooks **or** migrate the existing commit-automation service.
