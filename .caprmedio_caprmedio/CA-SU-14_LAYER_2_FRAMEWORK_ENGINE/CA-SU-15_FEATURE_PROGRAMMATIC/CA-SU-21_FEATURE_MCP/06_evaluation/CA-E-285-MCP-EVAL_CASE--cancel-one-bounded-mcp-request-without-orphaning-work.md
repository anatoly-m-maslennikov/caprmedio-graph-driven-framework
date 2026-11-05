---
atom_id: CA-E-285
ref_id: CA-E-285
container:
  scope_unit: CA-SU-21
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control
tier: 3
relations:
  evaluation_for:
  - CA-M-179
  derived_from:
  - CA-A-057
status: Active
version: 20
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
---
# Cancel one bounded MCP request without orphaning work

## Claim checked

MCP cancellation terminates one admitted bounded request **without** corrupting state **or** leaving ungoverned work.

## Test case

Cancel one admitted long-running request with a progress identity **before** its
declared completion boundary, **then** deliver one late downstream completion.

## Acceptance criteria

pass **only** **when** the adapter stops **or** isolates downstream work, releases bounded
resources, emits no successful terminal result, keeps Tool **and** project state
valid, **and** the late completion cannot revive the cancelled request.

## Failure disposition

Stop **and** diagnose the request boundary **before** another dispatch.

## Sources

- [Model Context Protocol: cancellation](https://modelcontextprotocol.io/specification/2024-11-05/basic/utilities/cancellation)
- [Model Context Protocol: tasks](https://modelcontextprotocol.io/specification/2025-11-25/basic/utilities/tasks)
- [CA-M-179 — Bound one admitted MCP request](../05_method/CA-M-179-MCP-ENG_DECISION--bound-one-admitted-mcp-request.md)
