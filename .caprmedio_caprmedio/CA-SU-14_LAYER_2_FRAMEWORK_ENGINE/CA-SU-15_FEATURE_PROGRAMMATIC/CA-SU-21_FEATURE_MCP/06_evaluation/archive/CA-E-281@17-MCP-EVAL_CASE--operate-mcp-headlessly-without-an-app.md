---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Entry
version: 17
updated_at: 2026-11-02 19:44:26 +0400
relations:
  evaluation_for:
  - CA-M-175
  derived_from:
  - CA-A-057
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-281
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: MCP
type: Eval Case
tier: 3
carrier_destination:
  file:
    name: CA-E-281@17-MCP-EVAL_CASE--operate-mcp-headlessly-without-an-app.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/06_evaluation/archive
---
# Operate MCP headlessly without an App

## Claim checked

the project-local provider-neutral MCP service exposes an eligible Tool **without** App **or** plugin presentation.

## Test case

Start the MCP service **without** `GRAPH_UI` **or** an agent-host plugin **and** invoke one eligible Tool, retrieve one ACTION_PROMPT invocation, **and** start one Workflow until its next interaction boundary.

## Acceptance criteria

the Tool remains discoverable **and** callable, the prompt returns its self-contained invocation envelope, **and** the Workflow returns its next resumable state through the one project-local service.

## Failure disposition

Reject an MCP deployment that depends on an App **or** transfers provider-neutral ownership **to** a plugin.
