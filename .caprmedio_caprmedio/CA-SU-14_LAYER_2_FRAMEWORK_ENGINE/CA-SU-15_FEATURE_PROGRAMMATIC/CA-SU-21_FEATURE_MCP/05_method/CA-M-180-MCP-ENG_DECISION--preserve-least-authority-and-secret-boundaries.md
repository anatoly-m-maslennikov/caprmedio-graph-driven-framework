---
cce_version: cce_1
cce_form: method
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Effect
    Authorization
version: 19
updated_at: 2026-11-02 19:44:26 +0400
relations:
  method_for:
  - CA-R-1118
  derived_from:
  - CA-A-057
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-M-180
ref_id: CA-M-180
status: Active
role: Method
author: Anatoly Maslennikov
current_scope_unit: MCP
form: Eng Decision
tier: 2
container:
  scope_unit: CA-SU-21
---
# Preserve least-authority and secret boundaries

## Applicable when

Apply **when** MCP projects a capability, forwards an invocation, **or** forms a result.

## Procedure

1. Grant no more authority than the source Tool requires **and** preserve its authorization checks.
2. Bind credentials **only** **to** their admitted transport **and** resource boundary.
3. Exclude secrets from discovery, results, diagnostics, logs, progress, **and** generated registries.

## Outcome

MCP exposes **only** the Tool's admitted authority **without** leaking credentials.

## Failure or stop

Stop the affected projection **or** invocation **when** authority is broadened **or** a secret-bearing representation would be emitted.

## Sources

- [Model Context Protocol: authorization](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)
- [CA-A-057 — Reconcile PROGRAMMATIC specialization authority](../../02_analysis/CA-A-057-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-programmatic-specialization-authority.md)
