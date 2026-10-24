---
subjects:
  governs: framework-engine-mcp
  depends_on: []
version: 13
updated_at: 2026-10-24 02:14:24 +0400
llm_session_ids:
- codex:01a01cb6-4ee4-7553-b68d-0823dda35094
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-1119
status: Active
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: MCP
type: Rule
tier: 1
---
# Return stable model-readable MCP results

MCP **must** map Tool results, diagnostics, empty results, partial results, **and** failures into stable model-readable protocol responses while preserving their governed meaning **and** provenance. Responses **must** remain usable **without** a user interface, distinguish protocol failure from Tool failure, **and** **must not** expose internal implementation details as part of the public MCP contract.
