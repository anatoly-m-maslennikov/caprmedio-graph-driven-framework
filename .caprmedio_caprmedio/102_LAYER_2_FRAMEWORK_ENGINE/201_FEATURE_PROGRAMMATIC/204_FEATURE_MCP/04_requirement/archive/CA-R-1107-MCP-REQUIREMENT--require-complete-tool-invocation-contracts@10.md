---
subjects:
  governs: "framework-engine-mcp"
  depends_on: []
version: 10
updated_at: 2026-10-11 01:09:00 +0400
llm_session_ids:
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Require complete Tool invocation contracts

**every** active Tool exposed through MCP **must** provide `describe_tool()` as one complete machine-invocation descriptor with `schema_version: 1`. The descriptor **must** contain the stable Tool identity **and** version, purpose, capability kind, canonical-model-derived accepted-input **and** structured-output model symbols, canonical callable entrypoint, Action binding, callable availability, admission conditions, effect **and** permission metadata, source pins, diagnostic **and** failure contract. A Workflow binding admitted through MCP **must** expose the same descriptor shape with its Workflow-specific callable binding. Missing, conflicting, **or** ambiguous descriptor fields make **that** capability invalid for MCP projection.

The descriptor schemas **must** be derived from the canonical Tool **or** Workflow model rather than maintained as a handwritten second schema. Descriptor discovery **and** validation describe capability availability only; they **must not** invoke a Tool, start **or** resume a Workflow, infer approval, **or** cause an effect.
