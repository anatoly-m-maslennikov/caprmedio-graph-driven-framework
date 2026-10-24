---
cce_version: cce_1
cce_form: method
subjects:
  governs: Subject/Domain/Node/Occurrent/Execution/Workflow Run
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Engineering/Tool//WORKFLOW_ORCHESTRATOR
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Subject/Domain/Node/Continuant/History/Journal
  - Subject/Domain/Node/Continuant/Projection
  - Implementation
version: 7
updated_at: 2026-10-24 02:14:24 +0400
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  method_for:
  - CA-R-1522
  - CA-R-1523
  - CA-R-1524
  relates_to:
  - CA-M-158
  - CA-M-222
atom_id: CA-M-302
status: Active
content_role: Method
author: Anatoly Maslennikov
current_scope_unit: WORKFLOW_ORCHESTRATOR
type: Eng Decision
tier: 4
---
# Separate Workflow coordination from Action execution

**to** implement WORKFLOW_ORCHESTRATOR, separate responsive coordination from long-running Action execution.

- use an on-demand local background service for coordination. an HTTP server, remote deployment, **or** graphical interface is **not** required by this Method.
- execute long-running **or** blocking Actions through bounded workers **or** subprocesses; waiting for external results **or** Operator input **must not** block the coordination interface.
- keep Workflow selection, transition, handoff, retry, **and** approval behavior driven by applicable methodology inputs rather than independently authored application branches.
- use stable request, Run, **and** dispatch identities with durable handoff recording, duplicate suppression, **and** the declared effect-safety mechanism. separate transient worker state from canonical Journal history **and** rebuildable views.
- keep client transport **and** worker adapters replaceable. select concrete libraries, wire formats, persistence Carriers, **and** resource limits through their applicable authority rather than assuming an unapproved default.

asynchronous coordination does **not** require **every** Action implementation **to** use asynchronous programming **or** execute concurrently. this Method does **not** install hooks **or** migrate the existing commit-automation service.
