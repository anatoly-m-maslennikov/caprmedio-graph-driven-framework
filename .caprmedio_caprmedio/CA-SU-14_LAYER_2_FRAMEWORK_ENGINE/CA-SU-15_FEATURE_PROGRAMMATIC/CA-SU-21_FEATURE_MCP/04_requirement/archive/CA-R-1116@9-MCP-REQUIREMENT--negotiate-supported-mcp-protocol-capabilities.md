---
subjects:
  governs: framework-engine-mcp
  depends_on: []
version: 9
updated_at: 2026-10-23 03:17:34 +0400
llm_session_ids:
- codex:01a01cb6-4ee4-7553-b68d-0823dda35094
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-1116@9
status: Archived
---
# Negotiate supported MCP protocol capabilities

MCP **must** declare its supported Model Context Protocol revision **and** capabilities **and** negotiate them during initialization. Unsupported revisions, incompatible required capabilities, **and** invalid lifecycle transitions **must** fail with explicit machine-readable diagnostics rather than silently changing behavior **or** accepting an undefined compatibility mode.
