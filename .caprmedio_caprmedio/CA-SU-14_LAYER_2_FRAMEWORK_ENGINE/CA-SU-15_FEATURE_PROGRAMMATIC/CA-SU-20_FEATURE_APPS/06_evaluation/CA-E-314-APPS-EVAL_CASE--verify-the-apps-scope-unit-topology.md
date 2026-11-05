---
cce_version: cce_1
cce_form: evaluation
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
version: 19
updated_at: 2026-11-03 23:17:14 +0400
relations:
  evaluation_for:
  - CA-M-196
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-314
ref_id: CA-E-314
status: Active
role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: APPS
form: Eval Case
tier: 3
container:
  scope_unit: CA-SU-20
---
# Verify the APPS Scope Unit topology

## Claim checked

CA-M-196 registers the four immediate unordered APPS units with distinct responsibilities **and** without project authority.

## Applicable when

Apply whenever an immediate APPS child's ownership, structural identity, responsibility boundary, **or** realization path changes.

## Test case

Examine the current active APPS authority and its child declarations, using derived representations only as supporting evidence. Exercise graph access once with `GRAPH_UI` absent.

## Acceptance criteria

`WORKBENCH`, `GRAPH_UI`, `WORKFLOW_ORCHESTRATOR`, **and** `AGENT_HOST_PLUGINS` are distinct immediate unordered APPS children. `WORKBENCH` operates headlessly for Tools **and** MCP; `GRAPH_UI` remains optional; orchestration state belongs to `WORKFLOW_ORCHESTRATOR`; **and** no child becomes project authority.

## Failure disposition

Reject the topology and preserve the examined authority, supporting evidence, **and** every missing, duplicate, dependent, **or** conflicting boundary.
