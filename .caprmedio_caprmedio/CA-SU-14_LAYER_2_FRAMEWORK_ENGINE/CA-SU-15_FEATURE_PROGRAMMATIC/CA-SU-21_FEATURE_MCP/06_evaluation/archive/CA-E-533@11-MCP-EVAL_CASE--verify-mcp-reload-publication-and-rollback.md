---
atom_id: CA-E-533@11
content_role: Evaluation
type: Eval Case
current_scope_unit: MCP
status: Archived
author: Anatoly Maslennikov
version: 11
updated_at: 2026-10-27 06:04:45 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Execution Control
  depends_on:
  - Subject/Graph Node/Implementation
  - Subject/Graph Node/Engineering/Verification/Dynamic Testing
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Domain/Continuant/Project
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Graph Node/Domain/Continuant/Atom
tier: 3
---
# Summary

Verify MCP reload publication and rollback

## Scope

server-side hot reload for the Project-local MCP gateway.

## Claim

the MCP Evaluation **must** verify implementation reload through the real stdio protocol with controlled mock implementations.

## Details

- keep one client connection open; call implementation A, reload B, then call B successfully without reconnect.
- add, remove **and** change a Tool contract; verify the published list **and** negotiated notification.
- submit syntax-invalid code, initialization failure, duplicate Tool names **and** invalid schemas; verify rejection **and** continued service from A.
- reload the same frontier twice; verify unchanged generation **and** no duplicate effects.
- submit an extra field, traversal path **or** alternate Project root; verify rejection before execution.
- distinguish sent notification from unconfirmed client refresh; mocks do **not** prove Codex desktop discovery.

