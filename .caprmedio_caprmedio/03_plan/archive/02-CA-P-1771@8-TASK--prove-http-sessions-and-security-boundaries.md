---
atom_id: CA-P-1771@8
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Archived
version: 8
updated_at: 2026-10-25 02:38:20 +0400
subjects:
  governs: Subject/Engineering/MCP/HTTP Access Boundary Evaluation
  depends_on:
  - Subject/Engineering/Implementation
  - Subject/Engineering/Implementation Evaluation
  - Subject/Engineering/Workflow
  - Subject/Engineering/Action
  - Subject/Domain/Node/Continuant/History/Journal
relations:
  is_decomposition_of:
  - CA-P-1756
  blocks:
  - CA-P-1772
tier: 3
---
# Summary

Prove HTTP sessions and security boundaries

## Objective

Prove HTTP sessions and security boundaries under the parent's exact source contract.

## Details

http_mcp_restore exclusively owns 204_MCP/tests/test_hot_reload_http.py and WORKFLOW_ORCHESTRATOR/tests/test_mcp_http_runtime.py; bounded corrections touch only P1770-owned files.

Estimated execution slice <=15 minutes. Preserve other workers' changes. Root alone owns index, commits and actual shared runtime effects. Tests and disposable smoke evidence are not release promotion.

## Definition of Done

Real host SDK discovery/calls/reload/drain/cleanup and every-request auth/Host/Origin/health tests pass.

## Pre-execution review

Root accepts this exclusive bounded assignment as the minimal current parent repair. Preserve installed N and truthful observed effects.

## Recorded verification

e63cb5457; real host SDK protocol/security and slow-child cleanup tests passed. This is not a real Docker acceptance receipt.
