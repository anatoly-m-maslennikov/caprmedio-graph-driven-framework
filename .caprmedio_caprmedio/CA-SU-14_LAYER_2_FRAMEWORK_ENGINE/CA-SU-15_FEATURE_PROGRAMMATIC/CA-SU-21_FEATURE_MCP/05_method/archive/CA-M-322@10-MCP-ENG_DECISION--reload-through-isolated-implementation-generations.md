---
atom_id: CA-M-322@10
content_role: Method
current_scope_unit: MCP
status: Archived
author: Anatoly Maslennikov
version: 10
updated_at: 2026-10-26 00:46:35 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Aspect/Execution Control
  depends_on:
  - Subject/Graph Node/Engineering/MCP
  - Subject/Graph Node/Engineering/MCP.Hot Reload
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Domain/Continuant/Project
  - Subject/Graph Node/Engineering/MCP/Implementation Reload
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Graph Node/Domain/Continuant/Atom
type: Eng Decision
tier: 3
---
# Summary

Reload through isolated implementation generations

## Scope

server-side hot reload for the Project-local MCP gateway.

## Claim

the MCP implementation **must** prepare reload candidates in isolated generations **and** atomically select a validated generation for new dispatch.

## Details

1. keep the stdio gateway, protocol session, reload control **and** fixed Project binding stable.
2. load candidate code **and** dependencies in a separate local implementation process, rather than mutating live imported modules with importlib.reload.
3. initialize the candidate without starting Workflows, workers **or** source mutations; obtain its complete Tool contracts **and** validate names, schemas **and** the fixed Project binding.
4. switch new dispatch to the candidate **only** after validation succeeds; preserve the old generation for admitted calls.
5. drain retired generations **after** their admitted calls finish; expose a bounded drain failure rather than silently terminating uncertain effects.
6. when preparation fails, discard the candidate **and** keep the current generation. when a published generation later fails, report affected calls honestly; never replay a mutating call automatically.
7. serialize reload requests **and** suppress duplicate request IDs; an unchanged implementation frontier is a no-op.

