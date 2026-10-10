---
subjects:
  governs: "framework-engine-mcp"
  depends_on: []
version: 11
updated_at: 2026-10-11 01:09:00 +0400
llm_session_ids:
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Require complete Tool invocation contracts

MCP **must** consume the transport-neutral Tool self-description required by CA-R-1064 **without** duplicating or changing its contract. MCP **must** project the canonical descriptor through one uniform provider invoke wrapper and add only MCP transport identity, protocol representation, and transport diagnostics. A Workflow binding admitted through MCP uses the same descriptor shape with its Workflow-specific callable binding. Missing, conflicting, **or** ambiguous descriptor fields make **that** capability invalid for MCP projection.

Descriptor discovery and validation describe capability availability only; they **must not** invoke a Tool, start **or** resume a Workflow, infer approval, or cause an effect.
