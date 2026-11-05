---
atom_id: CA-P-1770
ref_id: CA-P-1770
container:
  atom: CA-P-1756
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Engineering/MCP/HTTP endpoint/Gateway implementation
  dependencies:
  - Subject/Graph Node/Engineering/Implementation
  - Subject/Graph Node/Engineering/Evaluation
  - Subject/Graph Node/Engineering/Workflow
  - Subject/Graph Node/Engineering/Action
  - Subject/Graph Node/Domain/Continuant/History/Journal
tier: 3
relations:
  is_decomposition_of:
  - CA-P-1756
  blocks:
  - CA-P-1771
  - CA-P-1772
status: Done
version: 8
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 1-CA-P-1770-TASK--implement-the-opt-in-http-gateway.md
    path: .caprmedio_caprmedio/03_plan/done/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/done/13-CA-P-1756-TASK--restore-authenticated-http-mcp-and-protocol-coverage/done
work_sequence_number: 1
current_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
---
# Summary

Implement the opt-in HTTP gateway

## Objective

Implement the opt-in HTTP gateway under the parent's exact source contract.

## Details

http_mcp_restore exclusively owns 204_MCP/http_server.py, server.py, hot_reload.py and WORKFLOW_ORCHESTRATOR/docker/entrypoint.py, runtime.py, mcp-http.compose.yaml.

Estimated execution slice <=15 minutes. Preserve other workers' changes. Root alone owns index, commits and actual shared runtime effects. Tests and disposable smoke evidence are not release promotion.

## Definition of Done

The optional adapter and lifecycle honor R1884/1885 M341/342 D578; unchanged stdio regression passes.

## Pre-execution review

Root accepts this exclusive bounded assignment as the minimal current parent repair. Preserve installed N and truthful observed effects.

## Recorded verification

e63cb5457; the accepted optional adapter and lifecycle preserve stdio default and explicit HTTP configuration. Root's full 18-case transport/runtime suite passed.
