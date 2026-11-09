---
atom_id: CA-E-279@18
ref_id: CA-E-279@18
container:
  scope_unit: CA-SU-21
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication
tier: 3
relations:
  evaluation_for:
  - CA-M-173
  derived_from:
  - CA-A-057
status: Archived
version: 18
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
destination:
  file:
    name: CA-E-279@18-MCP-EVAL_CASE--preserve-canonical-tool-ownership-through-one-mcp-call.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/06_evaluation/archive
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
