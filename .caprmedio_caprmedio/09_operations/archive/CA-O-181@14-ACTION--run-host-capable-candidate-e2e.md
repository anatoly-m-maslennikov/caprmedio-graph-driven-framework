---
atom_id: CA-O-181@14
ref_id: CA-O-181@14
container:
  scope_unit: CA-SU-00
role: Operations
form: Action
topics:
  main_subject: Subject/caprmedio/Action//Run host-capable Candidate E2E
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Verification
  - Subject/CAPRMEDIO/Carrier/Docker Image
  - Subject/CAPRMEDIO/Carrier
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
tier: 3
status: Archived
version: 14
updated_at: 2026-11-02 19:46:47 +0400
carrier_destination:
  file:
    name: CA-O-181@14-ACTION--run-host-capable-candidate-e2e.md
    path: .caprmedio_caprmedio/09_operations/archive
current_scope_unit: caprmedio
author: Anatoly Maslennikov
---
# Summary

Run host-capable Candidate E2E

## Action

Run host-capable Candidate E2E **means** one explicitly authorized host-capable controller execution against CA-O-186's exact candidate image, package, source frontier and N/N+1 bindings.

## Details

The exact E2E inventory is: `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKFLOW_ORCHESTRATOR/tests/test_docker_e2e.py`, `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKFLOW_ORCHESTRATOR/tests/test_selected_workflows_docker_e2e.py`, and `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKFLOW_ORCHESTRATOR/tests/test_selected_query_mcp_e2e.py`. Every declared testcase in all three modules must terminal-pass; skipped, excluded, missing or zero-coverage testcase is non-pass. The frozen Docker worker has no Docker socket and cannot claim this phase. A registered explicit host-capable controller and its exact declared capability are required; missing, denied, unsafe, unavailable, stale, non-passing or unjournalable capability yields its actual non-pass outcome. This Action never selects N+1, promotes, retires, mutates sources, expands mounts, exposes credentials or substitutes a cached/focused result. It records one recoverable Journal result bound to the exact candidate and image identity.
