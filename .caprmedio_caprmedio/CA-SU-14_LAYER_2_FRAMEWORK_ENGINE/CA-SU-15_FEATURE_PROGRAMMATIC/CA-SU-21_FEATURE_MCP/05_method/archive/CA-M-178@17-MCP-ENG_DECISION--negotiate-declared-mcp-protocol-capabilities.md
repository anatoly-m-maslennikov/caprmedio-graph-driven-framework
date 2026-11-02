---
cce_version: cce_1
cce_form: method
subjects:
  governs: Subject/Graph Node/Engineering/Architecture/Communication
  depends_on: []
version: 17
updated_at: 2026-10-27 06:04:45 +0400
relations:
  method_for:
  - CA-R-1116
  derived_from:
  - CA-A-057
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-M-178@17
status: Archived
content_role: Method
author: Anatoly Maslennikov
current_scope_unit: MCP
type: Eng Decision
tier: 2
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
