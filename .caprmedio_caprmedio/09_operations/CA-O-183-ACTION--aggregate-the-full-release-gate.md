---
atom_id: CA-O-183
ref_id: CA-O-183
role: Operations
form: Action
current_scope_unit: caprmedio
status: Active
author: Anatoly Maslennikov
topics:
  main_subject: Subject/caprmedio/Action//Aggregate the full Release Gate
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification
  - Subject/CAPRMEDIO/Carrier/Docker Image
  - Subject/CAPRMEDIO/Carrier
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
version: 14
updated_at: 2026-11-02 19:46:47 +0400
tier: 3
container:
  scope_unit: CA-SU-00
carrier_destination:
  file:
    name: CA-O-183-CAPRMEDIO-ACTION--aggregate-the-full-release-gate.md
    path: .caprmedio_caprmedio/09_operations
---
# Summary

Aggregate the full Release Gate

## Action

Aggregate the full Release Gate **means** the read-only decision over the exact closed-unit, image-canary and host Candidate E2E receipts for one frozen N/N+1 candidate.

## Details

Every receipt must name the same candidate manifest, source frontier, compiled output, package, immutable image and parent lineage. The Unit receipt must cover every declared testcase except exactly `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKFLOW_ORCHESTRATOR/tests/test_docker_e2e.py`, `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKFLOW_ORCHESTRATOR/tests/test_selected_workflows_docker_e2e.py`, and `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKFLOW_ORCHESTRATOR/tests/test_selected_query_mcp_e2e.py`; the E2E receipt must cover every testcase in those exact three modules. Every declared testcase must terminal-pass: skipped, excluded, missing or zero-coverage testcase is non-pass. Missing, stale, mixed-candidate, partial or unjournalable evidence is non-pass. This Action creates no runtime/Skill selection, image removal, retry, Docker effect or new authority.
