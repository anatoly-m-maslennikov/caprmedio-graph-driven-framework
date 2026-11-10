---
atom_id: CA-E-311
ref_id: CA-E-311
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
    <+ Architecture <+ Communication
  dependencies:
  - MODEL//CAPRMEDIO <+ Projection
  - MODEL//CAPRMEDIO <+ Package/Project Package
tier: 5
relations:
  evaluation_for:
  - CA-M-193
status: Active
version: 24
updated_at: 2026-11-10 20:47:54 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: PROGRAMMATIC
destination:
  file:
    name: CA-E-311-PROGRAMMATIC-EVAL_CASE--verify-supply-the-active-tool-frontier-to-mcp.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
---
## Summary

Verify supply the active tool frontier to mcp

## Claim



### Prose Claim
#### Claim checked

one MCP frontier refresh deterministically distinguishes a valid active Tool,
a disabled Tool, **and** an invalid active Tool **without** changing Tool meaning.

#### Applicable conditions

apply **when** MCP builds **or** refreshes its callable frontier from TOOLS.

#### Test case

provide one valid active Tool with a machine contract, one explicitly disabled
Tool, **and** one active Tool with an invalid machine contract, **then** request one
frontier refresh.

#### Acceptance criteria

pass **only** **when** **=1** unchanged endpoint is projected for the valid active
Tool **in** the candidate, the disabled Tool is omitted, the invalid active Tool is reported
explicitly, **and** no call semantics **or** mechanics are duplicated **in** MCP.
because the candidate includes an invalid active Tool, the refresh **must not**
publish a new current registry **or** present a previous registry as current,
under CA-R-1110.

#### Failure disposition

reject the candidate frontier **and** preserve the preceding valid frontier bytes
for recovery **when** the complete projection cannot validate; retaining those
bytes does **not** establish currentness.

#### Sources

- [CA-M-193 — Supply the active Tool frontier to MCP](../05_method/CA-M-193-PROGRAMMATIC-ENG_DECISION--supply-the-active-tool-frontier-to-mcp.md)
