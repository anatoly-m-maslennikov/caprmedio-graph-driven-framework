---
atom_id: CA-R-2194
content_role: Requirement
type: Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Runtime
version: 3
updated_at: 2026-10-27 22:43:55 +0400
relations: {}
tier: 1
---
# Summary

Define Runtime

## Claim

Runtime **means** a live technical execution context for Implementation. a Runtime exists while its process is alive, including when that process is idle or waiting for work. when the process is no longer alive, that Runtime no longer exists.

## Semantics

A running Docker container is an example of a Runtime. A Runtime can remain alive while no Workflow, Step or Action is executing. An Execution is the work performed within the context. Stored descriptions and Journal records are not the Runtime itself.
