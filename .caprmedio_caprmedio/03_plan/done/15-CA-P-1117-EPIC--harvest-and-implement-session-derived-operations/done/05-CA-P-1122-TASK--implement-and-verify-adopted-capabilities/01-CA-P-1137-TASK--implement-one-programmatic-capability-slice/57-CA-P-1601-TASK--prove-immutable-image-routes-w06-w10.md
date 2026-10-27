---
atom_id: CA-P-1601
content_role: Plan
type: Plan
label: Task
work_sequence_number: 57
current_scope_unit: caprmedio
claim_target_scope_unit: WORKFLOW_ORCHESTRATOR
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Subject/Graph Node/Engineering/Workflow
  depends_on:
  - Subject/Graph Node/Engineering/Workflow
  - Subject/Graph Node/Engineering/Action
  - Subject/Graph Node/Engineering/Implementation
  - Subject/Graph Node/Engineering/Evaluation
  - Subject/Graph Node/Domain/Continuant/History/Journal
version: 7
updated_at: 2026-10-25 17:32:27 +0400
relations:
  is_decomposition_of:
  - CA-P-1137
  blocks:
  - CA-P-1519
tier: 3
---
# Summary

Prove immutable image routes W06 W10

## Objective

Within <=15 minutes, Execute W06–W10 through actual MCP, durable queue, fresh connections and strict native effects and shared Run lineage using the exact freshly built image; W09 is explicitly mock-not-live-llm.

## Details

Use image sha256:057792974dc2d81f84f99dee5535a44d5ee30513b03f6154381d99aa0bd558cd, declared dependency groups workflow-orchestrator and rmed-workflow-mcp, and separate disposable Runtime Projects. No host Engine mount, assertion relaxation, live CLI or permission bypass. Other independent batches are separate Tasks; coverage counts only the assigned cases.

## Saved frontier

The host driver could not start: the repository virtual environment contains no Python executable. Provisioning the declared groups also failed on distribution-cache directory rename with EPERM in the existing and fresh permitted temporary cache. These attempts stopped. The bundled runtime lacks MCP, PyYAML and DBOS. No actual-image case ran; image tag was unchanged. CA-C-449 preserves the blocker. Prepared harness source does not count as execution or completion.

## Definition of Done

The assigned current immutable-image cases have exact passing functional evidence, or remain unfinished with their precise protected blocker.
