---
atom_id: CA-M-174
ref_id: CA-M-174
container:
  scope_unit: CA-SU-21
role: Method
form: Eng Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
tier: 2
relations:
  method_for:
  - CA-R-1112
  derived_from:
  - CA-A-057
status: Active
version: 19
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: method
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
---
# Preserve one Tool contract and authority boundary

## Applicable when

Apply while MCP adapts one canonical Tool request **or** result **to** protocol transport.

## Procedure

1. Implement MCP as a replaceable protocol adapter **and** keep project meaning
   **and** business decisions outside the carrier.
2. Preserve accepted inputs, results, diagnostics, failures, target-set identity, **and** side-effect controls exactly.
3. Pass a CAPRMEDIO Markdown Atom Doer's sealed target set, expected revision **or** digest, Initiative action, **and** receipt through unchanged.
4. Keep Finder, Checker, **and** Doer boundaries intact; do **not** infer approval **or** turn a failed **or** partial result into success.

## Outcome

Transport changes representation **only**, never Tool authority **or** semantics.

## Failure or stop

Stop whenever protocol adaptation would broaden authority, alter cardinality, **or** obscure a Tool failure.

## Sources

- [Model Context Protocol: base protocol](https://modelcontextprotocol.io/specification/2025-06-18/basic/index)
- [PEP 544 — Protocols](https://peps.python.org/pep-0544/)
- [CA-A-057 — Reconcile PROGRAMMATIC specialization authority](../../02_analysis/CA-A-057-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-programmatic-specialization-authority.md)
