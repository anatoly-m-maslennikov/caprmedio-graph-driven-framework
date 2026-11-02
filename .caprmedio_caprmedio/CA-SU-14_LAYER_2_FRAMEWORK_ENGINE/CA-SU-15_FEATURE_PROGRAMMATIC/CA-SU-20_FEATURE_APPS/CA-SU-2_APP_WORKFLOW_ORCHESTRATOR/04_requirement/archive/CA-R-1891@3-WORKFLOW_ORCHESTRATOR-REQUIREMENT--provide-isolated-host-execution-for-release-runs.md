---
atom_id: CA-R-1891@3
content_role: Requirement
current_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: Archived
author: Anatoly Maslennikov
version: 3
updated_at: 2026-10-23 03:14:50 +0400
subjects:
  governs: Release Version/Host Executor
  depends_on:
  - Release Version
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Permission
  - Queue
  - DBOS
  - Docker Image
  - Subject/Domain/Node/Continuant/History/Journal
  - Source
  - Implementation
relations:
  relates_to:
  - CA-O-164
  - CA-R-1883
---
# Summary

provide isolated host execution for Release Runs

## Scope

the host execution capability for source-admitted Release Version Runs in WORKFLOW_ORCHESTRATOR.

## Claim

WORKFLOW_ORCHESTRATOR **must** provide a Release-only Host Executor that can run the admitted host-dependent gates while preserving the separate native **and** Docker execution boundaries.

## Details

- the capability uses the existing source-bound Release implementation, exact Operator authorization **and** canonical Journal recording.
- **only** a fresh admitted Release Run **or** an expressly authorized recovery of a Run already bound **to** this Host Executor can execute through it.
- worker startup remains explicit. startup creates no Run; it consumes no work from another executor's Queue.
- the ordinary Docker worker retains its existing isolation, with no host Docker socket added.
- an unavailable Host Executor blocks Release admission; another executor does **not** become an implicit fallback.
- this capability does **not** authorize promotion, image deletion **or** replay of an uncertain effect. those effects retain their existing gates.
