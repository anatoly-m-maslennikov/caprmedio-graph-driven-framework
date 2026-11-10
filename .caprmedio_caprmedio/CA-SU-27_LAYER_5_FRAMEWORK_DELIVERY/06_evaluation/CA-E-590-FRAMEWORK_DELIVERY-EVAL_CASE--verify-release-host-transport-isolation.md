---
atom_id: CA-E-590
ref_id: CA-E-590
container:
  scope_unit: CA-SU-27
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Verification/Dynamic
    Testing
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control/Effect
    Authorization
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Component
    Structure
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation/Code
  - Subject/CAPRMEDIO/Carrier
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
tier: 6
relations:
  evaluation_for:
  - CA-R-1891
  - CA-M-347
  - CA-D-583
status: Active
version: 18
updated_at: 2026-11-09 15:54:30 +0400
carrier_destination:
  file:
    name: CA-E-590-FRAMEWORK_DELIVERY-EVAL_CASE--verify-release-host-transport-isolation.md
    path: .caprmedio_caprmedio/CA-SU-27_LAYER_5_FRAMEWORK_DELIVERY/06_evaluation
current_scope_unit: FRAMEWORK_DELIVERY
author: Anatoly Maslennikov
---

## Summary

verify Release host transport isolation

## Claim

### Prose Claim

the Evaluation **must** verify that the direct host release entrypoint validates each Local or Public invocation and keeps its Project-local release effects separate from the Docker/MCP runtime.

## Details

### Scope

the direct host invocation boundary for Local and Public Release.

- accept valid Local and Public operation arguments only when their Project root and Run ID pass the entrypoint validation, and verify the matching release implementation receives those same values.
- reject an invalid root, symlink root or Run ID before Journal recording or release dispatch.
- verify the direct host implementation places Local Release runtime/report artifacts below `.caprmedio_runtime/simple_local_release/` and transient artifacts below `.caprmedio_tmp/simple_local_release/`, without making either authoring authority.
- verify the entrypoint does not create or call a Workflow Orchestrator Queue, worker, private IPC health exchange or DBOS Workflow.
- make Journal recording failure visible with the result while preserving the independently observed Local or Public Release outcome.
- distinguish focused and complete-suite local validation, Docker/MCP smoke, and Public Release checks. Each retains its own actual evidence; this Evaluation does not substitute one for another.
