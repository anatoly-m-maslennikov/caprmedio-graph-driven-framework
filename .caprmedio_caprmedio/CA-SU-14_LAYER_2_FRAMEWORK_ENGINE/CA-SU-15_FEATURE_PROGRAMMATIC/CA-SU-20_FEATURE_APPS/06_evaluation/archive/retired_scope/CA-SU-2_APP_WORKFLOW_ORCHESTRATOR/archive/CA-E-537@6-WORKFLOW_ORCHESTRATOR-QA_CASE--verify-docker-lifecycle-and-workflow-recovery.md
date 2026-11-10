---
atom_id: CA-E-537@6
content_role: Evaluation
type: Eval Case
current_scope_unit: WORKFLOW_ORCHESTRATOR
status: Archived
author: Anatoly Maslennikov
version: 6
updated_at: 2026-10-24 01:18:03 +0400
subjects:
  governs: Subject/Engineering/Runtime/Docker Lifecycle and Workflow Recovery
  depends_on:
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/History/Journal
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Engineering/Runtime/Docker Lifecycle and Workflow Recovery Evaluation
relations:
  evaluation_for:
  - CA-R-1818
  - CA-M-324
  - CA-D-525
  - CA-D-526
tier: 3
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
