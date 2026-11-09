---
atom_id: CA-M-180@19
ref_id: CA-M-180@19
container:
  scope_unit: CA-SU-21
role: Method
form: Eng Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution
    Control/Effect Authorization
tier: 2
relations:
  method_for:
  - CA-R-1118
  derived_from:
  - CA-A-057
status: Archived
version: 19
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: method
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
destination:
  file:
    name: CA-M-180@19-MCP-ENG_DECISION--preserve-least-authority-and-secret-boundaries.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/05_method/archive
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
