---
subjects:
  governs: Subject/Engineering/MCP
  depends_on: []
version: 14
updated_at: 2026-10-24 06:07:28 +0400
llm_session_ids:
- codex:01a01cb6-4ee4-7553-b68d-0823dda35094
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-1106@14
status: Archived
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: MCP
type: Rule
tier: 1
---
# Discover active Tool units

MCP **must** discover the complete current set of immediate Tool units owned by `TOOLS` from the current project graph **and** their corresponding Tool folders. Every registered immediate Tool unit is eligible for MCP exposure **unless** current project authority **or** Configuration explicitly disables it; nested implementation helpers **and** folders that are **not** Tool units **must not** become MCP tools.
