---
atom_id: CA-P-1603
ref_id: CA-P-1603
container:
  atom: CA-P-1137
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Engineering/Occurrent/Runtime/Docker Runtime
  dependencies:
  - Subject/Graph Node/Engineering/Workflow
  - Subject/Graph Node/Engineering/Action
  - Subject/Graph Node/Engineering/Implementation
  - Subject/Graph Node/Engineering/Evaluation
  - Subject/Graph Node/Domain/Continuant/History/Journal
tier: 3
relations:
  is_decomposition_of:
  - CA-P-1137
  blocks:
  - CA-P-1519
status: Active
version: 7
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 59-CA-P-1603-TASK--prove-immutable-image-source-and-mount-guards.md
    path: .caprmedio_caprmedio/03_plan/done/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/done/5-CA-P-1122-TASK--implement-and-verify-adopted-capabilities/1-CA-P-1137-TASK--implement-one-programmatic-capability-slice
work_sequence_number: 59
current_scope_unit: caprmedio
claim_target_scope_unit: WORKFLOW_ORCHESTRATOR
author: Anatoly Maslennikov
assignee: AI Agent
---
# Summary

Prove immutable image source and mount guards

## Objective

Within <=15 minutes, Run the current fresh-image no-host-Engine-mount and stale-source rejection tests through the actual declared host MCP driver.

## Details

Use image sha256:057792974dc2d81f84f99dee5535a44d5ee30513b03f6154381d99aa0bd558cd, declared dependency groups workflow-orchestrator and rmed-workflow-mcp, and separate disposable Runtime Projects. No host Engine mount, assertion relaxation, live CLI or permission bypass. Other independent batches are separate Tasks; coverage counts only the assigned cases.

## Saved frontier

The host driver could not start: the repository virtual environment contains no Python executable. Provisioning the declared groups also failed on distribution-cache directory rename with EPERM in the existing and fresh permitted temporary cache. These attempts stopped. The bundled runtime lacks MCP, PyYAML and DBOS. No actual-image case ran; image tag was unchanged. CA-C-449 preserves the blocker. Prepared harness source does not count as execution or completion.

## Definition of Done

The assigned current immutable-image cases have exact passing functional evidence, or remain unfinished with their precise protected blocker.
