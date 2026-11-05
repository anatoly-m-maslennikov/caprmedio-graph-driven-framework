---
cce_version: cce_1
cce_form: evaluation
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
version: 18
updated_at: 2026-11-02 19:44:26 +0400
relations:
  evaluation_for:
  - CA-M-178
  derived_from:
  - CA-A-057
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-398
ref_id: CA-E-398
status: Active
role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: MCP
form: Eval Case
tier: 3
container:
  scope_unit: CA-SU-21
---
# Negotiate one supported MCP capability set

## Claim checked

Supported MCP peers reach operation with exactly the declared negotiated
revision **and** capability set.

## Test case

Initialize the adapter once with a supported revision **and** capability set **and**
once with one unsupported required capability.

## Acceptance criteria

pass **only** **when** the supported peer reaches operation with exactly the negotiated
set **and** the unsupported peer receives a stable incompatibility response **before**
**any** capability executes.

## Failure disposition

Stop the affected session **before** registry use **or** Tool dispatch.

## Sources

- [Model Context Protocol: lifecycle](https://modelcontextprotocol.io/specification/2025-06-18/basic/lifecycle)
- [CA-M-178 — Negotiate declared MCP protocol capabilities](../05_method/CA-M-178-MCP-ENG_DECISION--negotiate-declared-mcp-protocol-capabilities.md)
