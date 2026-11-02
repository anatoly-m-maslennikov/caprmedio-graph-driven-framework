---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: Subject/Graph Node/Engineering/Continuant/Tool//WORKFLOW_ORCHESTRATOR.Goal
  depends_on:
  - Subject/Graph Node/Engineering/Workflow Orchestration/Run Execution Dispatch
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
version: 11
updated_at: 2026-10-25 17:32:27 +0400
relations: {}
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-1605@11
status: Archived
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: APPS
type: Goal
tier: 1
---
# Coordinate Workflow Runs

WORKFLOW_ORCHESTRATOR **must** own synchronous **and** asynchronous Workflow Run coordination, including interactive Step suspension, result submission, continuation, recovery, **and** next-Step selection from applicable methodology.
