---
atom_id: CA-R-1112
ref_id: CA-R-1112
container:
  scope_unit: CA-SU-21
role: Requirement
form: Rule
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
    <+ Architecture <+ Communication <+ Interface Contracts
  dependencies:
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution
    Control <+ Effect Authorization
tier: 1
relations:
  IS_REPLACEMENT_FOR:
  - CA-M-174
status: Active
version: 23
updated_at: 2026-11-10 20:47:54 +0400
author: Anatoly Maslennikov
current_scope_unit: MCP
destination:
  file:
    name: CA-R-1112-MCP-RULE--preserve-tool-contracts-and-authority.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/04_requirement
---

## Summary

Preserve Tool contracts and authority

## Claim

### Prose Claim

MCP **must** preserve each Tool's accepted inputs, structured outputs, diagnostics, failures, target-set identity, **and** side-effect controls **without** changing their meaning. MCP **must** preserve Finder read-only behavior, Checker evidence **and** verdict behavior, Doer dry-run **and** explicit-apply behavior, **and** **every** Tool permission boundary; it **must** never broaden mutation authority, infer approval, **or** convert a failed **or** partial Tool result into success.

For CAPRMEDIO Markdown Atom Doers, MCP **must** pass through the canonical Tool's sealed target set, expected revision **or** digest, Initiative action envelope, **and** resulting receipt. It **must not** replace a Tool's atomic **or** bulk cardinality, preflight, conflict, recovery, **or** lifecycle decision with transport behavior of its own.

## Details

Use MCP as a replaceable protocol adapter: pass the canonical request/result and Markdown Atom Doer's sealed target set, expected revision/digest, Initiative action envelope, and receipt unchanged. Stop when adaptation would broaden authority, alter cardinality, or obscure a Tool failure.
