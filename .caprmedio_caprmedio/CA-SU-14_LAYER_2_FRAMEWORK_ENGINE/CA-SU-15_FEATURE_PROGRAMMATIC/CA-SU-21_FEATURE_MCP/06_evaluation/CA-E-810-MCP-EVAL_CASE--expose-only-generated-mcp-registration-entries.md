---
atom_id: CA-E-810
ref_id: CA-E-810
container:
  scope_unit: CA-SU-21
role: Evaluation
form: Eval Case
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
    <+ Data Handling <+ Source Selection
tier: 3
relations:
  evaluation_for:
  - CA-R-3013
  IS_REPLACEMENT_FOR:
  - CA-E-274
  DERIVED_FROM:
  - CA-A-057
status: Active
version: 3
updated_at: 2026-11-10 20:47:54 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
destination:
  file:
    name: CA-E-810-MCP-EVAL_CASE--expose-only-generated-mcp-registration-entries.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/06_evaluation
---
## Summary

Expose only generated MCP registration entries

## Claim

### Prose Claim

Verify that MCP registration loads only installed code-owned provider entries from the generated registration asset. Helper modules and native Atom, Scope Unit or Tool folders do not select exposure.

## Details

Load an asset with an enabled provider, disabled configured entry and unlisted helper: only the enabled entry is exposed and the other dispositions are explicit. Missing or malformed configuration reports explicitly without native-source fallback. Verify that an installed registered Tool on the global exact-name `mcp_blacklist` is absent from tools/list and direct invocation rejects before provider dispatch; Project settings cannot re-enable it. Add a provider to prove admission follows generated configuration, not a gateway allowlist.
