---
atom_id: CA-R-1819@9
content_role: Requirement
current_scope_unit: WORKFLOW_ORCHESTRATOR
status: Archived
author: Anatoly Maslennikov
version: 9
updated_at: 2026-10-26 00:46:35 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Aspect/Execution Control
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: AI Agent'
  - Subject/Graph Node/Domain/Continuant/Atom
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  - Subject/Graph Node/Engineering/Agent Execution/Project-Write Isolation
  - Subject/Graph Node/Engineering/Continuant/Carrier
relations:
  relates_to:
  - CA-R-1814
  - CA-R-846
type: Rule
tier: 3
---
# Summary

isolate Agent proposals from Project writes

## Scope

Agentic Action execution **in** the Docker runtime.

## Claim

an AI Agent **must** receive **only** its supplied execution context **and** required authentication, **without** access **to** writable Project Carriers, the host home directory **or** the Docker daemon.

## Details

- the AI Agent returns a structured proposal; the trusted worker alone admits **and** applies authorized changes.
- the execution context carries the selected Atom, checking rules, Action prompt **and** relevant saved phase report.
- container isolation replaces the inner CLI sandbox **only** **in** the dedicated Agent service, which has no Project mounts.
- credentials remain runtime data, excluded from the image, source control, public status **and** reports.
