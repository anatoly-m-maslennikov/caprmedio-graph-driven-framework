---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Graph Node/Engineering/Aspect/Architecture/Communication
  depends_on: []
version: 15
updated_at: 2026-10-26 00:46:35 +0400
relations:
  evaluation_for:
  - CA-M-173
  derived_from:
  - CA-A-057
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-279@15
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: MCP
type: Eval Case
tier: 3
---
# Preserve canonical Tool ownership through one MCP call

## Claim checked

MCP delegates a call **without** reimplementing the canonical Tool's decisions **or** lifecycle behavior.

## Test case

Invoke one exposed Tool with a fixture that would reveal an MCP-side target **or** lifecycle decision.

## Acceptance criteria

**only** the canonical Tool performs that decision **and** MCP returns its resulting structured outcome unchanged.

## Failure disposition

Reject the transport implementation as an unauthorized second operation owner.
