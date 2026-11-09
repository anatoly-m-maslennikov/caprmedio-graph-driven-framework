---
atom_id: CA-E-399@18
ref_id: CA-E-399@18
container:
  scope_unit: CA-SU-21
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution
    Control/Effect Authorization
tier: 3
relations:
  evaluation_for:
  - CA-M-180
  derived_from:
  - CA-A-057
status: Archived
version: 18
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
destination:
  file:
    name: CA-E-399@18-MCP-EVAL_CASE--reject-one-unauthorized-mcp-capability-call.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/06_evaluation/archive
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
- [CA-M-180 — Preserve least authority and secret boundaries](../05_method/CA-M-180-MCP-ENG_DECISION--preserve-least-authority-and-secret-boundaries.md)
