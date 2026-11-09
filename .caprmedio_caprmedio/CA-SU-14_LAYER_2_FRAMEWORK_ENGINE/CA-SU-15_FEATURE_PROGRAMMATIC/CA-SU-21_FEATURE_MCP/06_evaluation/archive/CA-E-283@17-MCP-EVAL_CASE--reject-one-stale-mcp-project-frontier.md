---
atom_id: CA-E-283@17
ref_id: CA-E-283@17
container:
  scope_unit: CA-SU-21
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication
tier: 3
relations:
  evaluation_for:
  - CA-M-177
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
    name: CA-E-283@17-MCP-EVAL_CASE--reject-one-stale-mcp-project-frontier.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/06_evaluation/archive
---
# Reject one stale MCP project frontier

## Claim checked

An MCP invocation **must** bind **to** one current project, installed release, graph frontier, **and** registry revision.

## Test case

Invoke one Tool through a registry made stale by a changed project frontier.

## Acceptance criteria

MCP rejects the invocation explicitly **and** exposes enough provenance **to** identify the stale boundary.

## Failure disposition

Stop **before** Tool execution; do **not** guess a current release **or** project root.
