---
atom_id: CA-E-682
current_scope_unit: WORKBENCH_CODEX
claim_target_scope_unit: WORKBENCH_CODEX
status: Archived
version: 1
author: Anatoly Maslennikov
role: Evaluation
form: Eval Case
tier: 5
subjects:
  active: CAPRMEDIO_MODEL <+ Project
relations:
  evaluation_for:
  - CA-R-2791
  - CA-M-475
carrier_destination:
  file:
    name: CA-E-682@1-WORKBENCH_CODEX-EVAL_CASE--exercise-one-project-codex-conversation.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-47_FEATURE_WORKBENCH_CODEX/06_evaluation/archive
updated_at: 2026-11-05 14:23:38 +0400
---

## Summary

Exercise one Project Codex conversation

## Claim

### Prose Claim

When the official Codex app-server and Workbench bridge are available, test one selected Project through the Workbench interface. Verify that its one Workspace reaches the loopback bridge through HTTP and SSE from the exact origin derived from the selected Project MCP endpoint, with no wildcard CORS.

Verify that repeated `GET /conversation` opens or resumes the same native thread without creating a duplicate. Verify that `POST /turn` first emits a native `turn_id`, streams native events with the thread and turn IDs, and ends with exactly one `completed`, `failed` or `interrupted` terminal event. Verify that `POST /respond` returns an interaction or approval through its native request ID, and `POST /interrupt` affects only the matching active turn.

Verify that the conversation discovers CAPRMEDIO through the generated root `discover_tools` catalog and its current native frontier, discovers other enabled configured MCP servers natively, and can call one discovered CAPRMEDIO Tool with the explicit `project_root`. Verify that a requested Tool interaction or approval is presented to the Operator. Verify that the Docker Workbench has no Codex credentials and the runtime state exposes only the native thread ID. Do not assert private app-server implementation details.
