---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Engineering/MCP
  depends_on:
  - Subject/Domain/Node/Continuant/Projection
  - programmatic software
version: 17
updated_at: 2026-10-24 06:07:28 +0400
relations:
  evaluation_for:
  - CA-M-193
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-311@17
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: PROGRAMMATIC
type: Eval Case
tier: 5
---
# Verify supply the active tool frontier to mcp

## Claim checked

one MCP frontier refresh deterministically distinguishes a valid active Tool,
a disabled Tool, **and** an invalid active Tool **without** changing Tool meaning.

## Applicable conditions

apply **when** MCP builds **or** refreshes its callable frontier from TOOLS.

## Test case

provide one valid active Tool with a machine contract, one explicitly disabled
Tool, **and** one active Tool with an invalid machine contract, **then** request one
frontier refresh.

## Acceptance criteria

pass **only** **when** **=1** unchanged endpoint is projected for the valid active
Tool **in** the candidate, the disabled Tool is omitted, the invalid active Tool is reported
explicitly, **and** no call semantics **or** mechanics are duplicated **in** MCP.
because the candidate includes an invalid active Tool, the refresh **must not**
publish a new current registry **or** present a previous registry as current,
under CA-R-1110.

## Failure disposition

reject the candidate frontier **and** preserve the preceding valid frontier bytes
for recovery **when** the complete projection cannot validate; retaining those
bytes does **not** establish currentness.

## Sources

- [CA-M-193 — Supply the active Tool frontier to MCP](../05_method/CA-M-193-PROGRAMMATIC-METHOD--supply-the-active-tool-frontier-to-mcp.md)
