---
atom_id: CA-A-1226
ref_id: CA-A-1226
container:
  scope_unit: CA-SU-00
role: Analysis & Advisory
form: Specification Proposal
topics:
  main_subject: Subject
tier: 3
status: Done
version: 4
updated_at: 2026-11-02 15:49:28 +0400
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
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

[Rebuilt main Subject view](../../_projection/CA-PROJ-009-CAPRMEDIO--Subject-Graph--Current-RMEDO.md).
