---
atom_id: CA-R-1118
ref_id: CA-R-1118
container:
  scope_unit: CA-SU-21
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution
    Control/Effect Authorization
tier: 1
status: Active
version: 21
updated_at: 2026-11-09 21:15:45 +0400
llm_session_ids:
- codex:01a01cb6-4ee4-7553-b68d-0823dda35094
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
carrier_destination:
  file:
    name: CA-R-1118-MCP-RULE--enforce-least-authority-and-secret-boundaries.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/04_requirement
relations:
  IS_REPLACEMENT_FOR:
  - CA-M-180
---

## Summary

Enforce least authority and secret boundaries

## Claim

### Prose Claim

MCP **must** grant each projected capability no more authority than its source Tool requires **and** **must** preserve **all** Tool authorization **and** permission checks. Credentials **must** remain bound **to** their admitted transport **and** resource, **and** secrets **must not** appear **in** Tool discovery, model-readable results, diagnostics, logs, progress messages, **or** generated registries.

## Details

### Authorization and secrets

#### Applicable when

Apply **when** MCP projects a capability, forwards an invocation, **or** forms a result.

#### Procedure

1. Grant no more authority than the source Tool requires **and** preserve its authorization checks.
2. Bind credentials **only** **to** their admitted transport **and** resource boundary.
3. Exclude secrets from discovery, results, diagnostics, logs, progress, **and** generated registries.

#### Outcome

MCP exposes **only** the Tool's admitted authority **without** leaking credentials.

#### Failure or stop

Stop the affected projection **or** invocation **when** authority is broadened **or** a secret-bearing representation would be emitted.

#### Sources

- [Model Context Protocol: authorization](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)
- [CA-A-057 — Reconcile PROGRAMMATIC specialization authority](../../02_analysis/CA-A-057-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-programmatic-specialization-authority.md)
