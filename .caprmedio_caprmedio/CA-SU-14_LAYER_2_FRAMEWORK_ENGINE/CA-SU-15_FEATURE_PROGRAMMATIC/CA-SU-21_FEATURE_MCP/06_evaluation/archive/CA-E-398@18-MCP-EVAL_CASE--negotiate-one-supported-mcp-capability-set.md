---
atom_id: CA-E-398@18
ref_id: CA-E-398@18
container:
  scope_unit: CA-SU-21
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication
tier: 3
relations:
  evaluation_for:
  - CA-M-178
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
    name: CA-E-398@18-MCP-EVAL_CASE--negotiate-one-supported-mcp-capability-set.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/06_evaluation/archive
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
