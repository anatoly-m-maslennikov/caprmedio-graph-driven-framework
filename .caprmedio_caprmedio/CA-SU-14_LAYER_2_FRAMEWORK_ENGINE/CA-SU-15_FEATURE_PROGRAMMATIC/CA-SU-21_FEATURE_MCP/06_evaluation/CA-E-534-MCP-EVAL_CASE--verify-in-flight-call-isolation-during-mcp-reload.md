---
atom_id: CA-E-534
content_role: Evaluation
type: Eval Case
current_scope_unit: MCP
status: Active
author: Anatoly Maslennikov
version: 9
updated_at: 2026-10-27 19:59:37 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
tier: 3
---
# Summary

Verify in-flight call isolation during MCP reload

## Scope

server-side hot reload for the Project-local MCP gateway.

## Claim

the MCP Evaluation **must** verify that reload preserves admitted call identity, authority **and** truthful outcomes.

## Details

- hold a call on A while publishing B; verify that the old call completes on A **and** a new call executes on B.
- verify that old generations remain alive while their admitted calls are running.
- simulate child-process failure **after** a mutating call starts; verify an explicit uncertain outcome **and** no automatic replay.
- exercise concurrent reload requests, duplicate request IDs **and** drain limits; verify serialized publication **and** bounded explicit diagnostics.
- verify that reload does **not** start a Workflow, Codex Agent, independent worker **or** source mutation.
- verify that get_mcp_reload_status advertises read-only metadata **and** returns generation state without reload **or** persistence.
- verify that reload_mcp_implementation remains state-changing, rejects operation status **and** does **not** alter client permission settings.
- retain existing MCP request validation **and** Project-boundary regression tests.
