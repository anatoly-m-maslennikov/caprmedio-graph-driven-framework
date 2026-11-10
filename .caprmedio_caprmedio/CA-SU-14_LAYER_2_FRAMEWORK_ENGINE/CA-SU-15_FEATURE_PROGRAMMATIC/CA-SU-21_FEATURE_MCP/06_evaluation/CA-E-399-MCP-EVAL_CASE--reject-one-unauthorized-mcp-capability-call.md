---
atom_id: CA-E-399
ref_id: CA-E-399
container:
  scope_unit: CA-SU-21
role: Evaluation
form: Eval Case
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
    <+ Execution Control <+ Effect Authorization
tier: 3
relations:
  evaluation_for:
  - CA-R-1118
  DERIVED_FROM:
  - CA-A-057
status: Active
version: 21
updated_at: 2026-11-10 20:47:54 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
destination:
  file:
    name: CA-E-399-MCP-EVAL_CASE--reject-one-unauthorized-mcp-capability-call.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/06_evaluation
---

## Summary

Reject one unauthorized MCP capability call

## Claim

### Prose Claim

An MCP request **without** the required capability authority is rejected **before**
project access **and** does **not** expose **or** reuse credentials.

## Details

### Test case

Submit one structurally valid request whose authorization context lacks the
required permission **and** carries credentials for another resource.

### Acceptance criteria

pass **only** **when** the request is rejected **before** access, the protocol error is
stable, logs contain no token material, **and** the unrelated credential is **not**
used.

### Failure disposition

Stop the capability **and** treat **any** access **or** disclosure as an authority-boundary
defect.

### Sources

- [Model Context Protocol: authorization](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)
- [CA-R-1118 — Preserve least authority and secret boundaries](../04_requirement/CA-R-1118-MCP-RULE--enforce-least-authority-and-secret-boundaries.md)
