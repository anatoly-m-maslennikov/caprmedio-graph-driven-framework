---
subjects:
  governs: "framework-engine-mcp"
  depends_on: []
version: 9
updated_at: 2026-10-11 01:09:00 +0400
llm_session_ids:
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Regenerate the MCP registry deterministically

MCP registry generation **must** be a programmatic deterministic derivation from `schema_version: 1` capability descriptors in the activated installed runtime. It **must** resolve **and** seal the complete descriptor source frontier before publication, use stable ordering, and produce the same semantic registry from the same descriptors **and** activated Project state. It **must not** read a checkout as a live registry source, maintain a manually edited MCP-core allowlist, or execute a capability while generating the registry.

Repeated generation over an unchanged frontier **must** be idempotent, and volatile execution metadata **must not** change MCP capability identity **or** schema. A changed activated installed image **or** descriptor frontier creates a new registry generation; existing calls remain bound to their captured generation, and notification evidence **must** distinguish an emitted change notice from confirmed client refresh.
