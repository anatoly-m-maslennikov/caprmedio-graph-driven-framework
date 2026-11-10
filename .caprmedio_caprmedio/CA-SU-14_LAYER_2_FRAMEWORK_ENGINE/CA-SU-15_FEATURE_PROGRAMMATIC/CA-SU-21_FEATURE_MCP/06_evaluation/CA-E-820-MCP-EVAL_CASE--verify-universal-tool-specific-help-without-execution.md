---
atom_id: CA-E-820
ref_id: CA-E-820
container:
  scope_unit: CA-SU-21
role: Evaluation
form: Eval Case
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
    <+ Architecture <+ Communication
tier: 4
relations:
  evaluation_for:
  - CA-R-970308647
  - CA-M-548
  - CA-D-714
status: Active
version: 1
updated_at: 2026-11-11 00:16:05 +0400
author: Anatoly Maslennikov
current_scope_unit: MCP
destination:
  file:
    name: CA-E-820-MCP-EVAL_CASE--verify-universal-tool-specific-help-without-execution.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/06_evaluation
---

## Summary

Verify universal tool specific help without execution

## Claim

### Prose Claim

For every admitted public MCP Tool, call with `help: true` and no normal business inputs, using the required trusted Project envelope where applicable. Assert that only that Tool's purpose and usage, parameter formats and allowed values, minimal examples, output contract and common errors are returned and that these agree with the same generated registry's schema and metadata. Verify that a newly registered provider receives help through the shared layer without a central Tool-name allowlist or duplicate handwritten help description.

Instrument business validation and provider dispatch, query/query-run, Workflow execution, source writes, business gates and business Journal Run creation: all remain untouched for help, including Tools whose normal calls require inputs or would mutate data. Technical diagnostics may be recorded. Verify invalid or mismatched binding rejects without cross-Project fallback, and that global blacklist and Project exclusions prevent direct help from exposing unavailable Tools. Verify normal calls still enforce their own business validation.

Send the minimal help-shaped request through each registered public MCP Tool boundary, with the required Project envelope and no business inputs; assert protocol schema acceptance and the specified response, rather than testing only the internal help handler.
