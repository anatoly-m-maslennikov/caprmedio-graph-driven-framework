---
subjects:
  governs: "framework-engine-mcp"
  depends_on: [Tool, Model, Implementation, Admission, Operator]
relations:
  relates_to: [CA-R-1930]
version: 12
updated_at: "2026-10-11 01:19:56 +0400"
llm_session_ids:
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Require complete Tool invocation contracts

MCP **must** consume the transport-neutral Tool self-description required by `CA-R-1930-TOOLS-CORE-REQUIREMENT--require-uniform-tool-self-description` **without** duplicating or changing its contract. MCP **must** project the canonical descriptor through one uniform provider invoke wrapper and add only MCP transport identity, protocol representation, and transport diagnostics. A Workflow binding admitted through MCP is outside this Tool descriptor contract. Missing, conflicting, **or** ambiguous Tool descriptor fields make **that** Tool invalid for MCP projection.

Descriptor discovery and validation describe capability availability only; they **must not** invoke a Tool, start **or** resume a Workflow, infer approval, or cause an effect.
