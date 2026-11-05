---
cce_version: cce_1
cce_form: obligation
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Effect Authorization
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
version: 15
updated_at: 2026-10-29 22:26:56 +0400
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-1605
ref_id: CA-R-1605
status: Active
role: Requirement
author: Anatoly Maslennikov
current_scope_unit: WORKFLOW_ORCHESTRATOR
form: Rule
tier: 0
claim_target_scope_unit: WORKFLOW_ORCHESTRATOR
container:
  scope_unit: CA-SU-2
carrier_destination:
  file:
    name: CA-R-1605-WORKFLOW_ORCHESTRATOR-SCOPE_CONTRACT-RULE--coordinate-workflow-runs.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-2_APP_WORKFLOW_ORCHESTRATOR/04_requirement
---
## Summary

Coordinate Workflow Runs

## Claim

WORKFLOW_ORCHESTRATOR **must** own synchronous **and** asynchronous Workflow Run coordination, including interactive Step suspension, result submission, continuation, recovery, **and** next-Step selection from applicable methodology.
