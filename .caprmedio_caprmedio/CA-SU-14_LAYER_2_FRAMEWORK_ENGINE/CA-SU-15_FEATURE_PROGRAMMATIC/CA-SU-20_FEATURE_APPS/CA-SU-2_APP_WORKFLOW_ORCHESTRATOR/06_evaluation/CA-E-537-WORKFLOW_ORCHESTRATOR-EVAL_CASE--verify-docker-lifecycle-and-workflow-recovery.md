---
atom_id: CA-E-537
ref_id: CA-E-537
container:
  scope_unit: CA-SU-2
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Recovery
tier: 4
relations:
  evaluation_for:
  - CA-R-1818
  - CA-M-324
  - CA-D-525
  - CA-D-526
status: Active
version: 12
updated_at: 2026-10-27 19:59:37 +0400
carrier_destination:
  file:
    name: CA-E-537-WORKFLOW_ORCHESTRATOR-EVAL_CASE--verify-docker-lifecycle-and-workflow-recovery.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-2_APP_WORKFLOW_ORCHESTRATOR/06_evaluation
current_scope_unit: WORKFLOW_ORCHESTRATOR
author: Anatoly Maslennikov
---
# Summary

verify Docker lifecycle **and** Workflow recovery

## Scope

the Docker runtime's mocked end-to-end **and** lifecycle tests.

## Claim

the Evaluation **must** verify that Docker lifecycle operations preserve authorized Workflow behavior **and** durable evidence **without** dispatch duplication.

## Details

- build the image **and** start a mock Agent plus real DBOS worker; verify current readiness rather than container existence alone.
- enqueue through MCP, disconnect the client, observe completion, confirmed Journal events **and** a full report.
- restart the worker **and** verify persistence of terminal results **without** another Agent call.
- interrupt an in-flight dispatch **and** verify recovery reports uncertainty rather than replaying it.
- verify stopped Docker routing fails visibly **and** leaves the native queue untouched.
- run mocks **without** live credentials **or** paid model calls; distinguish this evidence from a separately authorized real Agent pilot.
