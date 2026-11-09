---
atom_id: CA-D-548@12
ref_id: CA-D-548@12
container:
  scope_unit: CA-SU-21
role: Delivery
form: Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Entry
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Component
    Structure
tier: 4
relations:
  delivery_for:
  - CA-R-1847
  - CA-R-1848
status: Archived
version: 12
updated_at: 2026-11-09 07:45:14 +0400
carrier_destination:
  file:
    name: CA-D-548@12-MCP-DECISION--preserve-existing-mcp-helpers-and-hot-reload.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/07_delivery/archive
current_scope_unit: MCP
claim_target_scope_unit: MCP
author: Anatoly Maslennikov
---

## Summary

Preserve existing MCP helpers and hot reload

## Claim

### Prose Claim

Selected adapters **must** be additive and reload-compatible; they **must not** replace the stable gateway, its root binding, or its eight existing helpers.

## Details

### Scope

Compatibility of selected MCP adapters with the stable gateway and existing helper surface.

Implementation registers the declared routes through `create_server(root)` after
root resolution and uses the current stdio transport and stable hot-reload
boundary. It preserves `discover_tools`, `discover_operations`,
`get_execution_context`, `get_execution_status`, `resume_execution_context`,
`watch_execution`, `rmed_atoms_base_revise`, and `workflow_orchestrator` with
their current names and contracts. `workflow_orchestrator` remains the general
selected-queue entrypoint for an admitted `enqueue_selected` request; it does
not itself become a per-route executor. Only a selected route whose configured
execution binding is absent is blocked or deferred. That absence does not
disallow an otherwise accepted general selected-queue request, including either
admitted read-only query route once its exact binding is implemented.

Reload validates a complete new route registry before publication, keeps in-flight calls on their captured implementation generation, and rolls back invalid registration without removing prior helpers. After code-owned registration selects an exposed route, validate that route's current admitted source binding before dispatch. Reject or defer stale or unsupported bindings without changing Tool exposure. MCP code contains adapter/validation/projection logic only; the common `RUN_SUPPORT` interface owns lifecycle execution, durable event retries, and canonical Journal persistence.

#### Sources

- CA-D-523 v2; CA-E-533 v1; CA-E-534 v1; CA-A-1141 v1 K7/K16; CA-D-521 v3.
