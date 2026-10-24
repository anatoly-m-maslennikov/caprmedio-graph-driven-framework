---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: framework-engine-mcp
  depends_on: []
version: 9
updated_at: 2026-10-24 02:14:24 +0400
relations:
  evaluation_for:
  - CA-M-180
  derived_from:
  - CA-A-057
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-399
status: Active
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: MCP
type: Eval Case
tier: 3
---
# Reject one unauthorized MCP capability call

## Claim checked

An MCP request **without** the required capability authority is rejected **before**
project access **and** does **not** expose **or** reuse credentials.

## Test case

Submit one structurally valid request whose authorization context lacks the
required permission **and** carries credentials for another resource.

## Acceptance criteria

pass **only** **when** the request is rejected **before** access, the protocol error is
stable, logs contain no token material, **and** the unrelated credential is **not**
used.

## Failure disposition

Stop the capability **and** treat **any** access **or** disclosure as an authority-boundary
defect.

## Sources

- [Model Context Protocol: authorization](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)
- [CA-M-180 — Preserve least authority and secret boundaries](../05_method/CA-M-180-MCP-CORE-METHOD--preserve-least-authority-and-secret-boundaries.md)
