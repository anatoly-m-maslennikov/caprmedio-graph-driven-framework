---
atom_id: CA-E-277
ref_id: CA-E-277
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
  - CA-R-1109
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
    name: CA-E-277-MCP-EVAL_CASE--remove-one-disabled-tool-projection.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/06_evaluation
---

## Summary

Remove one disabled Tool projection

## Claim

### Prose Claim

Verify that rebuilding the registration asset after a configured provider or route is disabled removes that callable identity while retaining every other eligible configured entry.

## Details

Disable a previously exposed configured entry and rebuild the asset. The registry excludes it and retains all other eligible configured entries; no stale exposure remains.
