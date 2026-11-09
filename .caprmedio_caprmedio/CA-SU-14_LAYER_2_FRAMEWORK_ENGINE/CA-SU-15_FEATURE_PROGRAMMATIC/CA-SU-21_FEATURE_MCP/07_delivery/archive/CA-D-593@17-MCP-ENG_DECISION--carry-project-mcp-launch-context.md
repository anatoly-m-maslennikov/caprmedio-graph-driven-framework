---
atom_id: CA-D-593@17
ref_id: CA-D-593@17
container:
  scope_unit: CA-SU-21
role: Delivery
form: Eng Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Settings
  - Scope Unit
  - Subject/CAPRMEDIO/Carrier
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Component
    Structure
tier: 5
relations:
  delivery_for:
  - CA-R-1900
  - CA-M-355
status: Archived
version: 17
updated_at: 2026-11-05 13:48:40 +0400
carrier_destination:
  file:
    name: CA-D-593@17-MCP-ENG_DECISION--carry-project-mcp-launch-context.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/07_delivery/archive
current_scope_unit: MCP
author: Anatoly Maslennikov
---

## Summary

Carry Project MCP launch context

## Claim

The launcher **must** carry one explicit ProjectSelection record whose identity and selected bindings are sufficient to isolate the MCP Gateway and launcher state. The record carries the canonical host Project root, selected control root, Project identity, container path mapping and selected manifest, registry and query-source references.

The Codex hook's top-level project_root is an optional assertion for single-Project Tool calls and a required assertion for shared-Project Tool calls. Validate it against the carried ProjectSelection before Tool dispatch. A malformed or mismatched assertion produces a safe refusal with no native Tool execution, source effect or Journal effect. Remove the assertion envelope before a native Tool receives its own arguments. Prompt and Workflow wrappers retain their normal dispatch; initialize and tools/list are protocol operations, not Tool-call envelopes.

tools/list **must** advertise the top-level project_root input as optional for the single-Project service and required for the shared service, without mutating the native Tool descriptors or their input schemas. The advertisement describes the service boundary only; native Tool arguments remain unchanged.

Place launcher-owned Gateway context, hot-reload receipts, cache metadata, pending-launch evidence and the per-Project lock under the selected Project's installed runtime state in an identity-named namespace. Gateway and reload constructors consume the carried selection rather than scanning for a default control root or repository ancestor. A Carrier records safe identifiers and relative references, never credentials or an unselected Project's content.

This Carrier delivers no proxy, listener, worker, queue, Workflow request or Release transition. Shared delivery may serve multiple explicit Projects through one endpoint, but each request remains bound to its validated ProjectSelection.
