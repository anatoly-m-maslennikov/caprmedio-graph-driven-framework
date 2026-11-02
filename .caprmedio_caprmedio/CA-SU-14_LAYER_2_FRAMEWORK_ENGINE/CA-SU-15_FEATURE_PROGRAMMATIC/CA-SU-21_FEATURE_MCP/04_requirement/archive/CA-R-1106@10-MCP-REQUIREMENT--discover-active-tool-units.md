---
subjects:
  governs: framework-engine-mcp
  depends_on: []
version: 10
updated_at: 2026-10-24 00:28:02 +0400
llm_session_ids:
- codex:01a01cb6-4ee4-7553-b68d-0823dda35094
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-1106@10
status: Archived
---
# Discover active Tool units

MCP **must** discover the complete current set of immediate Tool units owned by `TOOLS` from the current project graph **and** their corresponding Tool folders. Every registered immediate Tool unit is eligible for MCP exposure **unless** current project authority **or** Configuration explicitly disables it; nested implementation helpers **and** folders that are **not** Tool units **must not** become MCP tools.
