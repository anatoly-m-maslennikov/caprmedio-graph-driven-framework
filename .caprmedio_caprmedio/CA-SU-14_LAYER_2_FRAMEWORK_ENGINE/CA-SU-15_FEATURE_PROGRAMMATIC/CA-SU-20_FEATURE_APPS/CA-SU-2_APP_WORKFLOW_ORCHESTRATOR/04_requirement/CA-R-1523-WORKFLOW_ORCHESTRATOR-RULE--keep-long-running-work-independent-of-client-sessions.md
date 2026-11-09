---
atom_id: CA-R-1523
ref_id: CA-R-1523
container:
  scope_unit: CA-SU-2
role: Requirement
form: Rule
topics:
  {"main_subject": "CAPRMEDIO_MODEL <+ Entity/Object/Occurrent/Execution/Workflow Run", "dependencies": ["CAPRMEDIO_MODEL <+ Atom/(.Header.Role:=Operations)/Workflow", "CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Action", "CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator", "CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Term//Artifact", "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control/Recovery"]}
tier: 1
status: Active
version: 15
updated_at: 2026-10-27 19:59:57 +0400
cce_version: cce_1
cce_form: obligation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: WORKFLOW_ORCHESTRATOR
---
## Summary

Keep long-running work independent of client sessions

## Claim

### Prose Claim

WORKFLOW_ORCHESTRATOR **must** keep accepted work independent of the lifetime of the client session that submitted it.

- submission returns an identifier for accepted work **without** waiting for the Workflow **or** a long-running Action **to** finish.
- the Operator **or** an authorized client can inspect progress, results, failures, **and** pending decisions; supply requested input; request cancellation; **and** reconnect **to** the same accepted work.
- acceptance, a cancellation request, **and** actual completion are distinct outcomes. disconnecting a client **must not** silently cancel work **or** make unfinished work appear successful.
- waiting for an Action **or** Operator input **must not** prevent the application from reporting state **or** accepting admitted control requests.
- asynchronous submission does **not** itself authorize parallel Actions, concurrent mutation of an Artifact, **or** execution outside the applicable permissions.

the result **must** disclose an unsupported control **or** execution capability rather than imply it was performed.
