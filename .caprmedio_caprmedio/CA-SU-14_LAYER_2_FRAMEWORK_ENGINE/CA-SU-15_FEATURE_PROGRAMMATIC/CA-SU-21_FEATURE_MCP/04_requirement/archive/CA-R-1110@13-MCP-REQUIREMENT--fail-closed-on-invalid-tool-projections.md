---
subjects:
  governs: framework-engine-mcp
  depends_on: []
version: 13
updated_at: 2026-10-24 01:28:26 +0400
llm_session_ids:
- codex:01a01cb6-4ee4-7553-b68d-0823dda35094
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-1110@13
status: Archived
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: MCP
type: Rule
---
# Fail closed on invalid Tool projections

MCP **must** fail closed for each invalid Tool **or** Workflow descriptor. A missing contract field, name collision, invalid canonical-model-derived schema, unresolved binding, **or** ambiguous capability identity **must** make only that capability unavailable with explicit diagnostics. MCP **must not** expose the invalid capability, retain its stale projection as current, **or** reinterpret it as another capability.

MCP **must** publish the complete set of independently valid current descriptors despite an unrelated invalid descriptor. One quarantined capability **must not** disable, withdraw, **or** misrepresent an unrelated valid Tool **or** Workflow binding. Registry output **must** identify each unavailable capability and its attributable diagnostic without claiming that client refresh has occurred.
