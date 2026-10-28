---
atom_id: CA-O-181
content_role: Operations
type: Action
current_scope_unit: caprmedio
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Subject/caprmedio/Action//Run host-capable Candidate E2E
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification
  - Subject/CAPRMEDIO/Carrier/Docker Image
  - Subject/CAPRMEDIO/Carrier
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
version: 13
updated_at: 2026-10-27 19:59:47 +0400
relations: {}
tier: 3
---
# Summary

Run host-capable Candidate E2E

## Action

Run host-capable Candidate E2E **means** one explicitly authorized host-capable controller execution against CA-O-186's exact candidate image, package, source frontier and N/N+1 bindings.

## Details

The exact E2E inventory is: `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_docker_e2e.py`, `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_selected_workflows_docker_e2e.py`, and `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_selected_query_mcp_e2e.py`. Every declared testcase in all three modules must terminal-pass; skipped, excluded, missing or zero-coverage testcase is non-pass. The frozen Docker worker has no Docker socket and cannot claim this phase. A registered explicit host-capable controller and its exact declared capability are required; missing, denied, unsafe, unavailable, stale, non-passing or unjournalable capability yields its actual non-pass outcome. This Action never selects N+1, promotes, retires, mutates sources, expands mounts, exposes credentials or substitutes a cached/focused result. It records one recoverable Journal result bound to the exact candidate and image identity.
