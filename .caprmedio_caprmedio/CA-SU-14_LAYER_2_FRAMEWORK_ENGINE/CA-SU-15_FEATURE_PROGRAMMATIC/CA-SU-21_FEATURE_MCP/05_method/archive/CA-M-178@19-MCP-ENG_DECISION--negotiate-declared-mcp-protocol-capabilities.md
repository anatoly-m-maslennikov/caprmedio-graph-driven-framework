---
atom_id: CA-M-178@19
ref_id: CA-M-178@19
container:
  scope_unit: CA-SU-21
role: Method
form: Eng Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication
tier: 2
relations:
  method_for:
  - CA-R-1116
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
    name: CA-M-178@19-MCP-ENG_DECISION--negotiate-declared-mcp-protocol-capabilities.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/05_method/archive
---
# Negotiate declared MCP protocol capabilities

## Applicable when

Apply during MCP service initialization.

## Procedure

1. Declare the supported protocol revision **and** capability set.
2. Compare the peer's required revision **and** capabilities with that declaration.
3. Accept **only** a defined compatible mode **and** return machine-readable diagnostics for unsupported **or** invalid lifecycle states.

## Outcome

MCP initialization selects one explicit compatible protocol boundary.

## Failure or stop

Stop on an unsupported revision, incompatible required capability, **or** invalid lifecycle transition.

## Sources

- [Model Context Protocol: lifecycle](https://modelcontextprotocol.io/specification/2025-06-18/basic/lifecycle)
- [CA-A-057 — Reconcile PROGRAMMATIC specialization authority](../../02_analysis/CA-A-057-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-programmatic-specialization-authority.md)
