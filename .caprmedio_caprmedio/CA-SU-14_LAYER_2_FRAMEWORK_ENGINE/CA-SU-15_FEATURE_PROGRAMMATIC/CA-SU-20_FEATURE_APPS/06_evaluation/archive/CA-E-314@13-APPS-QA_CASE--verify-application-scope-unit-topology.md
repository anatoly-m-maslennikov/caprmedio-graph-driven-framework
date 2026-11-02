---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Domain/Node/Continuant/Scope Unit
  depends_on: []
version: 13
updated_at: 2026-10-24 11:29:41 +0400
relations:
  evaluation_for:
  - CA-M-196
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-314@13
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: APPS
type: Eval Case
tier: 3
---
# Verify the APPS Scope Unit topology

## Claim checked

CA-M-196 registers the four immediate unordered APPS units with distinct responsibilities **and** without project authority.

## Applicable when

Apply whenever an immediate APPS child's ownership, structural identity, responsibility boundary, **or** realization path changes.

## Test case

Examine the current active APPS authority and its child declarations, using derived representations only as supporting evidence. Exercise graph access once with `GRAPH_UI` absent.

## Acceptance criteria

`GRAPH_SERVER`, `GRAPH_UI`, `WORKFLOW_ORCHESTRATOR`, **and** `AGENT_HOST_PLUGINS` are distinct immediate unordered APPS children. `GRAPH_SERVER` operates headlessly for Tools **and** MCP; `GRAPH_UI` remains optional; orchestration state belongs to `WORKFLOW_ORCHESTRATOR`; **and** no child becomes project authority.

## Failure disposition

Reject the topology and preserve the examined authority, supporting evidence, **and** every missing, duplicate, dependent, **or** conflicting boundary.
