---
atom_id: CA-R-1116
ref_id: CA-R-1116@21
container:
  scope_unit: CA-SU-21
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication/Interface
    Contracts
tier: 1
relations:
  IS_REPLACEMENT_FOR:
  - CA-M-178
status: Archived
version: 21
updated_at: 2026-11-09 19:30:15 +0400
llm_session_ids:
- codex:01a01cb6-4ee4-7553-b68d-0823dda35094
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
destination:
  file:
    name: CA-R-1116@21-MCP-RULE--negotiate-supported-mcp-protocol-capabilities.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/04_requirement/archive
---

## Summary

Negotiate supported MCP protocol capabilities

## Claim

### Prose Claim

MCP **must** declare its supported Model Context Protocol revision **and** capabilities **and** negotiate them during initialization. Unsupported revisions, incompatible required capabilities, **and** invalid lifecycle transitions **must** fail with explicit machine-readable diagnostics rather than silently changing behavior **or** accepting an undefined compatibility mode.

## Details

Compare the peer's required protocol revision and capabilities with the declaration before capability execution.

### Sources

- [Model Context Protocol: lifecycle](https://modelcontextprotocol.io/specification/2025-06-18/basic/lifecycle)
- [CA-A-057 — Reconcile PROGRAMMATIC specialization authority](../02_analysis/CA-A-057-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-programmatic-specialization-authority.md)
