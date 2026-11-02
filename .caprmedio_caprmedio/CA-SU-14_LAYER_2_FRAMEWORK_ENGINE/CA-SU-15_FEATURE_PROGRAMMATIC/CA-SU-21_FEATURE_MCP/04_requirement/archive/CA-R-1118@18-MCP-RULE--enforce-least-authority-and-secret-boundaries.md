---
subjects:
  governs: Subject/Graph Node/Engineering/Execution Control/Effect Authorization
  depends_on: []
version: 18
updated_at: 2026-10-27 06:04:45 +0400
llm_session_ids:
- codex:01a01cb6-4ee4-7553-b68d-0823dda35094
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-1118@18
status: Archived
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: MCP
type: Rule
tier: 1
---
# Enforce least authority and secret boundaries

MCP **must** grant each projected capability no more authority than its source Tool requires **and** **must** preserve **all** Tool authorization **and** permission checks. Credentials **must** remain bound **to** their admitted transport **and** resource, **and** secrets **must not** appear **in** Tool discovery, model-readable results, diagnostics, logs, progress messages, **or** generated registries.
