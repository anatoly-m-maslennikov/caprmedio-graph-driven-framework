---
atom_id: CA-R-1891@17
content_role: Requirement
current_scope_unit: WORKFLOW_ORCHESTRATOR
status: Archived
author: Anatoly Maslennikov
version: 17
updated_at: 2026-10-27 06:04:45 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Execution Control
  depends_on:
  - Subject/Graph Node/Engineering/Architecture/Communication
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Engineering/Execution Control/Effect Authorization
  - Subject/Graph Node/Engineering/Architecture/Component Structure
  - Subject/Graph Node/Carrier/Docker Image
  - Subject/Graph Node/Domain/Continuant/History/Journal
  - Subject/Graph Node/Runtime
relations: {}
tier: 3
type: Rule
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
