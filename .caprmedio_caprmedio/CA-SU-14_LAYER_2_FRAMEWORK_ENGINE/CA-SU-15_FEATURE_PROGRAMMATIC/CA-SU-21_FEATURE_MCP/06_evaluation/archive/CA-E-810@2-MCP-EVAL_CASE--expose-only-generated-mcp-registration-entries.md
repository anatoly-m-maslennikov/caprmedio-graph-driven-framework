---
atom_id: CA-E-810
ref_id: CA-E-810@2
container:
  scope_unit: CA-SU-21
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Source
    Selection
tier: 3
relations:
  evaluation_for:
  - CA-R-3013
  derived_from:
  - CA-A-057
  IS_REPLACEMENT_FOR:
  - CA-E-274
status: Archived
version: 2
updated_at: 2026-11-09 21:15:45 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
destination:
  file:
    name: CA-E-810@2-MCP-EVAL_CASE--expose-only-generated-mcp-registration-entries.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/06_evaluation/archive
---

## Summary

Expose only generated MCP registration entries

## Claim

### Prose Claim

Verify that MCP registration loads only installed code-owned provider entries from the generated registration asset. Helper modules and native Atom, Scope Unit or Tool folders do not select exposure.

## Details

Load a generated asset containing an enabled provider, a disabled configured entry and an unlisted helper. Only the enabled configured entry is exposed; the other dispositions are explicit. Missing or malformed registration configuration is reported without falling back to native source discovery.

Cover an installed registered Tool on the explicit global `mcp_blacklist`: its descriptor is absent from tools/list and direct invocation is rejected before provider dispatch. A Project setting cannot re-enable it. Repeat with a newly added provider to prove admission follows the generated configuration rather than a hardcoded gateway allowlist.
