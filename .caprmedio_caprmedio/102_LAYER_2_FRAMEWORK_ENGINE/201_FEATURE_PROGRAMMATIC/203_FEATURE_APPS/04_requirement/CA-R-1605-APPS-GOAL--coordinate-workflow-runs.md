---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Effect Authorization
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
version: 14
updated_at: 2026-10-27 19:59:58 +0400
relations: {}
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-1605
status: Active
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: APPS
type: Goal
tier: 1
---
# Coordinate Workflow Runs

WORKFLOW_ORCHESTRATOR **must** own synchronous **and** asynchronous Workflow Run coordination, including interactive Step suspension, result submission, continuation, recovery, **and** next-Step selection from applicable methodology.
