---
atom_id: CA-R-1107
ref_id: CA-R-1107
container:
  scope_unit: CA-SU-21
role: Requirement
form: Rule
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
    <+ Architecture <+ Communication <+ Interface Contracts
  dependencies:
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling
    <+ Serialization
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution
    Control <+ Effect Authorization
  - MODEL//CAPRMEDIO <+ Actor/Operator
tier: 1
relations:
  IS_REPLACEMENT_FOR:
  - CA-M-169
status: Active
version: 31
updated_at: 2026-11-10 20:47:54 +0400
llm_session_ids:
- codex:01a01cb6-4ee4-7553-b68d-0823dda35094
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
destination:
  file:
    name: CA-R-1107-MCP-RULE--require-complete-tool-invocation-contracts.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/04_requirement
---

## Summary

Require complete Tool invocation contracts

## Claim

### Prose Claim

MCP **must** consume the transport-neutral Tool self-description required by `CA-R-1930-TOOLS-RULE--require-uniform-tool-self-description` **without** duplicating or changing its contract. MCP **must** project the canonical descriptor through one uniform provider invoke wrapper and add only MCP transport identity, protocol representation, and transport diagnostics. A Workflow binding admitted through MCP is outside this Tool descriptor contract. Missing, conflicting, **or** ambiguous Tool descriptor fields make **that** Tool invalid for MCP projection.

Descriptor discovery and validation describe capability availability only; they **must not** invoke a Tool, start **or** resume a Workflow, infer approval, or cause an effect.

## Details

Before exposure, call the Tool's canonical describe_tool() from trusted installed Engine code, resolve model symbols/provider adapter there, and derive schemas from canonical models. Validate every descriptor field against the same Tool identity; reject handwritten duplicate schemas, missing/conflicting/ambiguous fields, or unresolved entrypoints with field-level diagnostics. The affected descriptor is unavailable; validation neither repairs/reinterprets it, imports untrusted code, nor invokes a Tool or Workflow.
