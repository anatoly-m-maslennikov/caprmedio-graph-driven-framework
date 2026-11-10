---
atom_id: CA-E-275
ref_id: CA-E-275@20
container:
  scope_unit: CA-SU-21
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication
tier: 3
relations:
  evaluation_for:
  - CA-R-1107
  derived_from:
  - CA-A-057
status: Archived
version: 20
updated_at: 2026-11-09 19:30:15 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
destination:
  file:
    name: CA-E-275@20-MCP-EVAL_CASE--reject-one-incomplete-tool-invocation-contract.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/06_evaluation/archive
---

## Summary

Reject one incomplete Tool invocation contract

## Claim

### Prose Claim

MCP exposes **only** a complete coherent canonical descriptor with `schema_version: 1`.

## Details

### Test case

Validate one Tool descriptor missing a required CA-D-621 field beside one complete Tool descriptor. Repeat with a handwritten duplicate input schema, an unresolved callable entrypoint, and a missing Action binding.

### Acceptance criteria

The defective Tool returns a field-level unavailable diagnostic and produces no eligible projection. The independent complete Tool remains eligible. The harness proves models are imported from canonical symbols and that validation never invokes or applies either Tool.

### Failure disposition

Stop exposure of the affected descriptor **until** its contract is complete, canonical-model-derived, **and** unambiguous.
