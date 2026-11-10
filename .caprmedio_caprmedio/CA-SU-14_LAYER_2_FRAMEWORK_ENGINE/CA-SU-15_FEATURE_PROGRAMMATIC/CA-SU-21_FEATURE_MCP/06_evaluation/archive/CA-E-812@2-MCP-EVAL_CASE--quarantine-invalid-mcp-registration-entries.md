---
atom_id: CA-E-812
ref_id: CA-E-812@2
container:
  scope_unit: CA-SU-21
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Data
    Validation
tier: 3
relations:
  evaluation_for:
  - CA-R-1110
  derived_from:
  - CA-A-057
  IS_REPLACEMENT_FOR:
  - CA-E-278
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
    name: CA-E-812@2-MCP-EVAL_CASE--quarantine-invalid-mcp-registration-entries.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/06_evaluation/archive
---

## Summary

Quarantine invalid MCP registration entries

## Claim

### Prose Claim

Verify that an invalid descriptor is quarantined with an explicit diagnostic while independently valid descriptors publish. Unresolved generator integrity or the common activated descriptor frontier stops publication.

## Details

Introduce one invalid descriptor alongside an independent valid descriptor. Report and quarantine the invalid one and publish the valid one. Separately verify that a broken generator or unresolved common descriptor frontier prevents activation.
