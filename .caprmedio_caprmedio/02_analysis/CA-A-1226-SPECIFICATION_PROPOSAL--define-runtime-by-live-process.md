---
atom_id: CA-A-1226
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Subject
version: 2
updated_at: 2026-10-27 22:47:33 +0400
relations: {}
tier: 3
---
# Summary

Define Runtime by a live process

## Question

Does a Runtime continue to exist while it is idle?

## Operator decision

“if some process is alive, yes. if no, then no. we have docker container running”

A Runtime exists while its process is alive. Being idle or waiting for work does not end that Runtime. When its process is no longer alive, the Runtime no longer exists. A running Docker container is the concrete example.

## Scope

This resolves C10-I06 / C10-G04 by clarifying the existing Runtime definition. It does not add a lifecycle entity, mandatory process field, readiness test, health check or runtime implementation change.

## Adoption result

Current R2194@3 defines Runtime by a live process, including idle time, and retains the running Docker container example. Its predecessor is archived.

[Rebuilt main Subject view](../_projection/CA-PROJ-009-CAPRMEDIO--Subject-Graph--Current-RMEDO.md).
