---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control
  depends_on: []
version: 19
updated_at: 2026-10-27 19:59:50 +0400
llm_session_ids:
- codex:01a01cb6-4ee4-7553-b68d-0823dda35094
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-1117
status: Active
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: MCP
type: Rule
tier: 1
---
# Bound and control MCP requests

MCP **must** validate **every** admitted protocol message **before** dispatch, apply declared time **and** resource bounds, support cancellation **without** corrupting Tool **or** project state, **and** expose progress for admitted long-running operations. Invalid, expired, cancelled, **or** resource-exhausted requests **must** terminate with explicit structured outcomes **and** **must not** leave an ungoverned background operation.
