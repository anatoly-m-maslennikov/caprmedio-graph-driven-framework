---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
version: 26
updated_at: 2026-11-03 23:17:14 +0400
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-1100
status: Active
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: APPS
type: Definition
tier: 1
---
# Define the APPS Scope Unit topology

`APPS` **must** own the following immediate `unordered_unit` Scope Units: `WORKBENCH`, `GRAPH_UI`, `WORKFLOW_ORCHESTRATOR`, **and** `AGENT_HOST_PLUGINS`.

- `WORKBENCH` owns the headless source indexer, rebuildable graph read model, **and** read-only query service derived from governed Atoms **and** Journals.
- `GRAPH_UI` owns the optional human interface over `WORKBENCH` **and** **must not** be required for headless Tool or MCP operation.
- `WORKFLOW_ORCHESTRATOR` owns Workflow Run coordination, interactive Step suspension, continuation, **and** recovery.
- `AGENT_HOST_PLUGINS` owns host-specific integration packages.

None of these applications, their databases, interfaces, or Projections becomes project authority.
