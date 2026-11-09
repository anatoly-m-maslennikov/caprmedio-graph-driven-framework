---
atom_id: CA-R-1112@21
ref_id: CA-R-1112@21
container:
  scope_unit: CA-SU-21
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication/Interface
    Contracts
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control/Effect
    Authorization
tier: 1
status: Archived
version: 21
updated_at: 2026-11-02 19:44:26 +0400
llm_session_ids:
- codex:01a01cb6-4ee4-7553-b68d-0823dda35094
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
destination:
  file:
    name: CA-R-1112@21-MCP-RULE--preserve-tool-contracts-and-authority.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/04_requirement/archive
---
## Summary

Preserve Tool contracts and authority

## Claim

### Prose Claim

MCP **must** preserve each Tool's accepted inputs, structured outputs, diagnostics, failures, target-set identity, **and** side-effect controls **without** changing their meaning. MCP **must** preserve Finder read-only behavior, Checker evidence **and** verdict behavior, Doer dry-run **and** explicit-apply behavior, **and** **every** Tool permission boundary; it **must** never broaden mutation authority, infer approval, **or** convert a failed **or** partial Tool result into success.

For CAPRMEDIO Markdown Atom Doers, MCP **must** pass through the canonical Tool's sealed target set, expected revision **or** digest, Initiative action envelope, **and** resulting receipt. It **must not** replace a Tool's atomic **or** bulk cardinality, preflight, conflict, recovery, **or** lifecycle decision with transport behavior of its own.
