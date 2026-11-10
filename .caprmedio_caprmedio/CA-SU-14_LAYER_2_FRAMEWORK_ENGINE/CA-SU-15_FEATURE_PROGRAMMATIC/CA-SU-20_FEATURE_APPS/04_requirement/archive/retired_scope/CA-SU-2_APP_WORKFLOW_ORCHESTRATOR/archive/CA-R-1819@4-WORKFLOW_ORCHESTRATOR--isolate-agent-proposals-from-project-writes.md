---
atom_id: CA-R-1819@4
content_role: Requirement
current_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: Archived
author: Anatoly Maslennikov
version: 4
updated_at: 2026-10-23 03:14:50 +0400
subjects:
  governs: Subject/Engineering/Agent Execution/Project-Write Isolation
  depends_on:
  - 'Subject/Domain/Node/Continuant/Actor/Type: AI Agent'
  - Subject/Domain/Node/Continuant/Atom
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Implementation
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - Subject/Engineering/Agent Execution/Project-Write Isolation
  - Subject/Engineering/Carrier
relations:
  relates_to:
  - CA-R-1814
  - CA-R-846
type: Rule
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
