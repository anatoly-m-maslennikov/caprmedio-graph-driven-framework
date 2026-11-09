---
atom_id: CA-E-284@17
ref_id: CA-E-284@17
container:
  scope_unit: CA-SU-21
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication
tier: 3
relations:
  evaluation_for:
  - CA-M-178
  derived_from:
  - CA-A-057
status: Archived
version: 17
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
destination:
  file:
    name: CA-E-284@17-MCP-EVAL_CASE--reject-one-incompatible-mcp-protocol-initialization.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/06_evaluation/archive
---
# Reject one incompatible MCP protocol initialization

## Claim checked

MCP initialization admits **only** a declared compatible protocol revision **and** capability set.

## Test case

Initialize with one unsupported required protocol capability.

## Acceptance criteria

Initialization fails with a machine-readable incompatibility diagnostic **and** no undefined compatibility mode.

## Failure disposition

Stop the session **before** registry use **or** Tool dispatch.
