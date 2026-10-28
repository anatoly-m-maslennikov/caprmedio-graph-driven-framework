---
atom_id: CA-E-583@16
content_role: Evaluation
type: Eval Case
current_scope_unit: WORKFLOW_ORCHESTRATOR
status: Archived
author: Anatoly Maslennikov
version: 16
updated_at: 2026-10-27 06:04:45 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Execution Control
  depends_on:
  - Subject/Graph Node/Engineering/Execution Control/Recovery
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  - Subject/Graph Node/Domain/Occurrent/Execution/Step Run
  - Subject/Graph Node/Domain/Occurrent/Execution/Action Run
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Engineering/Execution Control/Effect Authorization
  - Subject/Graph Node/Domain/Continuant/History/Journal
  - Subject/Graph Node/Engineering/Execution Control
  - Subject/Graph Node/Implementation/Code
relations:
  evaluation_for:
  - CA-R-1883
  - CA-M-340
  - CA-D-577
tier: 6
---
# Summary

verify explicit frozen Release recovery

## Scope

the typed recovery admission and continuation boundary for one existing **CA-O-164** Release Workflow Run.

## Claim

the Evaluation **must** verify that Release recovery accepts only the exact frozen Run and preserves canonical Journal identity without replaying uncertain effects or creating extra Run facts.

## Details

- submit a recovery request for an existing interrupted Release Run and verify the sealed request identity, source freshness and current route-bound Operator authorization are required.
- submit a different Run ID, changed request identity, stale source, revoked permission, unknown field or arbitrary continuation payload and verify recovery blocks before an effect, start or terminal Journal event.
- recover one valid sealed pending Action event and verify the shared recorder appends its original bytes and receipt only. Verify changed Run, phase, outcome, result reference or effect reference blocks recovery.
- reopen a completed Workflow and verify it returns its original terminal result with no new Workflow, Step or Action start or terminal event.
- present an unresolved in-progress or uncertain effect and verify recovery returns blocked or pending without native effect replay. Verify queue and DBOS records do not override the canonical Journal.
- observe one queued recovery transport, then its success or failure, and verify the exact returned handle and frozen Run binding are required. Verify the original Run's cached DBOS result is reported only as canonical history, never as the recovery transport result. Also submit a recovery whose scheduler response is immediately successful, failed or canceled and verify it has a transport-only disposition, not a claim of canonical completion.
