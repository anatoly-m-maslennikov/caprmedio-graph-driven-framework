---
atom_id: CA-E-454
ref_id: CA-E-454
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Component
    Structure
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Settings
  - Subject/CAPRMEDIO/Carrier
tier: 5
relations:
  evaluation_for:
  - CA-M-284
  derived_from:
  - CA-A-053
status: Active
version: 21
updated_at: 2026-11-09 14:19:14 +0400
cce_version: cce_1
cce_form: evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
destination:
  file:
    name: CA-E-454-PROGRAMMATIC-EVAL_CASE--use-one-settings-reader-across-engine-software.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
---

## Summary

Use one Settings Reader across Engine software

## Claim

### Prose Claim

Verify that applicable Tool, App and MCP consumers use an immutable, validated settings snapshot with actual values, the selected Project, physical source path, raw SHA-256 digest and declared schema marker.

## Details

### Test case


Use a recording fake for the shared Reader and exercise representative applicable Tool, App and MCP consumers from each relevant PROGRAMMATIC child feature. A feature with no settings-dependent consumer adds no artificial test fixture.

### Acceptance criteria



Pass only when the Reader validates the complete input and returns the declared immutable snapshot with actual values, selected Project, source path, raw SHA-256 digest and schema marker. Each exercised consumer receives it explicitly, preserves its provenance, and performs no direct read, fallback, private default selection or mutation. Component-specific interpretation stays outside the Reader. The Reader does not query the Work Journal or infer logical currentness. A consumer may reuse an already validated snapshot; no per-consumer read count is imposed.

### Failure disposition

reject the bypassing consumer **until** it accepts the shared snapshot explicitly.

### Sources

- [Python documentation: `unittest.mock`](https://docs.python.org/3.14/library/unittest.mock.html)
- [CA-M-284 — Read Engine settings through one shared boundary](../05_method/CA-M-284-PROGRAMMATIC-DIRECT_POLICY--read-engine-settings-through-one-shared-boundary.md)
