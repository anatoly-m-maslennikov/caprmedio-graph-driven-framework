---
atom_id: CA-D-583
ref_id: CA-D-583
container:
  scope_unit: CA-SU-27
role: Delivery
form: Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution
    Control
  dependencies:
  - Subject/CAPRMEDIO/Carrier
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Storage/Directory Layout
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation/Code
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
tier: 5
relations:
  delivery_for:
  - CA-R-1891
  - CA-M-347
status: Active
version: 15
updated_at: 2026-11-09 15:54:30 +0400
carrier_destination:
  file:
    name: CA-D-583-FRAMEWORK_DELIVERY-DECISION--store-release-host-state-in-an-isolated-namespace.md
    path: .caprmedio_caprmedio/CA-SU-27_LAYER_5_FRAMEWORK_DELIVERY/07_delivery
current_scope_unit: FRAMEWORK_DELIVERY
author: Anatoly Maslennikov
---

## Summary

store Release host state in an isolated namespace

## Claim

### Prose Claim

the direct host release implementation's mutable delivery artifacts **must** remain below the resolved Project root in `.caprmedio_runtime/` or `.caprmedio_tmp/`, separate from authoring sources and Docker/MCP runtime state.

## Details

### Scope

the Local and Public Release artifacts written by the direct host implementation.

- Local Release writes its installed runtime package and reports below `.caprmedio_runtime/simple_local_release/` and uses `.caprmedio_tmp/simple_local_release/` only for temporary staging and test output.
- Public Release writes an input-required report below `.caprmedio_tmp/public_release/<run-id>/` when it needs content input.
- all locations are derived from the resolved Project root and must remain project-relative. They do not create a Workflow Orchestrator namespace, scheduler database, worker lock, Queue, DBOS store or private IPC carrier.
- reports and temporary artifacts describe delivery results; they do not become authoring authority or a second Journal.
- the Docker/MCP runtime remains independently packaged and managed by the release implementation.
