---
atom_id: CA-E-398
ref_id: CA-E-398@20
container:
  scope_unit: CA-SU-21
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication
tier: 3
relations:
  evaluation_for:
  - CA-R-1116
  derived_from:
  - CA-A-057
  IS_REPLACEMENT_FOR:
  - CA-E-284
status: Archived
version: 20
updated_at: 2026-11-09 19:30:15 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
destination:
  file:
    name: CA-E-398@20-MCP-EVAL_CASE--negotiate-one-supported-mcp-capability-set.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/06_evaluation/archive
---

## Summary

Negotiate one supported MCP capability set

## Claim

### Prose Claim

Supported MCP peers reach operation with exactly the declared negotiated
revision **and** capability set.

## Details

### Test case

Initialize the adapter once with a supported revision **and** capability set **and**
once with one unsupported required capability.

### Acceptance criteria

pass **only** **when** the supported peer reaches operation with exactly the negotiated
set **and** the unsupported peer receives a stable incompatibility response **before**
**any** capability executes.

### Failure disposition

Stop the affected session **before** registry use **or** Tool dispatch.

### Sources

- [Model Context Protocol: lifecycle](https://modelcontextprotocol.io/specification/2025-06-18/basic/lifecycle)
- [CA-R-1116 — Negotiate supported MCP protocol capabilities](../04_requirement/CA-R-1116-MCP-RULE--negotiate-supported-mcp-protocol-capabilities.md)
