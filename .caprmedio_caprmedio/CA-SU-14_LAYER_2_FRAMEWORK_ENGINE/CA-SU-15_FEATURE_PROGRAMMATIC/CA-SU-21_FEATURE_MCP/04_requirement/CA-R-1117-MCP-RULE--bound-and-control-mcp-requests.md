---
atom_id: CA-R-1117
ref_id: CA-R-1117
container:
  scope_unit: CA-SU-21
role: Requirement
form: Rule
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
    <+ Execution Control <+ Resource Limits
tier: 1
status: Active
version: 22
updated_at: 2026-11-10 20:47:54 +0400
llm_session_ids:
- codex:01a01cb6-4ee4-7553-b68d-0823dda35094
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
carrier_destination:
  file:
    name: CA-R-1117-MCP-RULE--bound-and-control-mcp-requests.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/04_requirement
relations:
  IS_REPLACEMENT_FOR:
  - CA-M-179
---

## Summary

Bound and control MCP requests

## Claim

### Prose Claim

MCP **must** validate **every** admitted protocol message **before** dispatch, apply declared time **and** resource bounds, support cancellation **without** corrupting Tool **or** project state, **and** expose progress for admitted long-running operations. Invalid, expired, cancelled, **or** resource-exhausted requests **must** terminate with explicit structured outcomes **and** **must not** leave an ungoverned background operation.

## Details

### Cancellation and request bounds

#### Applicable when

Apply **when** MCP receives one protocol message **before** Tool dispatch.

#### Procedure

1. Validate the message against the admitted schema **and** assign its declared
   time **and** resource bounds.
2. Expose progress **only** for an admitted long-running operation.
3. On cancellation, expiry, invalid input, **or** resource exhaustion, stop with a structured outcome **and** preserve Tool **and** project state.

#### Outcome

**every** MCP request has an explicit admission **and** completion boundary.

#### Failure or stop

Stop **before** dispatch on an invalid **or** expired request **and** never leave an ungoverned background operation.

#### Sources

- [Model Context Protocol: base protocol](https://modelcontextprotocol.io/specification/2025-06-18/basic/index)
- [Model Context Protocol: tasks](https://modelcontextprotocol.io/specification/2025-11-25/basic/utilities/tasks)
- [CA-A-057 — Reconcile PROGRAMMATIC specialization authority](../../02_analysis/CA-A-057-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-programmatic-specialization-authority.md)
