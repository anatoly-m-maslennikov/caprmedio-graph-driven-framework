---
subjects:
  governs: framework-engine-mcp
  depends_on: []
version: 12
updated_at: 2026-10-24 01:28:26 +0400
llm_session_ids:
- codex:01a01cb6-4ee4-7553-b68d-0823dda35094
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-1109@12
status: Archived
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: MCP
type: Rule
---
# Reconcile disabled and removed Tools

MCP regeneration **must** add **every** newly active valid Tool, exclude **every** explicitly disabled Tool, **and** remove **every** projection whose source Tool is no longer active **or** present. MCP **must not** maintain a second independent allowlist **or** lifecycle registry that can disagree with current project authority **and** Configuration.
