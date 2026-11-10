---
atom_id: CA-E-282
ref_id: CA-E-282
container:
  scope_unit: CA-SU-21
role: Evaluation
form: Eval Case
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
    <+ Data Handling <+ Output Publication
tier: 3
relations:
  evaluation_for:
  - CA-R-1114
  DERIVED_FROM:
  - CA-A-057
status: Active
version: 20
updated_at: 2026-11-10 20:47:54 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
destination:
  file:
    name: CA-E-282-MCP-EVAL_CASE--rebuild-one-unchanged-mcp-registry-identically.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/06_evaluation
---

## Summary

Rebuild one unchanged MCP registry identically

## Claim

### Prose Claim

Verify that rebuilding MCP registration from unchanged installed provider code, code-owned inventory and configuration yields the same callable identities and schemas. Volatile execution metadata does not change registration.

## Details

### Test case

Generate the registry twice from the same installed provider code, code-owned inventory and configuration.

### Acceptance criteria

the two registries have the same capability identities **and** schemas; volatile execution metadata does **not** change that result.

### Failure disposition

Stop publication **and** report the first nondeterministic configured entry or ordering defect.
