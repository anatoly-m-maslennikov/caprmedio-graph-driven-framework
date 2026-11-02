---
atom_id: CA-R-1820@4
content_role: Requirement
current_scope_unit: MCP
claim_target_scope_unit: MCP
status: Archived
author: Anatoly Maslennikov
version: 4
updated_at: 2026-10-24 11:58:20 +0400
subjects:
  governs: Subject/Engineering/MCP/Implementation Reload
  depends_on:
  - Subject/Engineering/MCP
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Subject/Domain/Node/Continuant/Project
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Domain/Node/Continuant/Atom
type: Rule
tier: 3
---
# Summary

reload MCP implementation **without** disconnecting

## Scope

server-side hot reload for the Project-local MCP gateway.

automatic file watching **and** operating-system startup hooks are outside this initial capability.

## Claim

the MCP gateway **must** provide Operator-requested implementation reload while preserving the established transport connection **and** its fixed Project boundary.

the reload capability has these required outcomes:

- a successful reload makes **`=1`** validated implementation generation available for new calls.
- a failed reload retains the previously serving generation **and** reports the failure.
- an in-flight call retains its admitted generation **until** it finishes; reload does **not** replay, cancel **or** migrate that call.

## Details

- reload **only** changes executable capability availability; it grants **no** new authority **to** mutate Atoms, start Workflows **or** launch workers.

