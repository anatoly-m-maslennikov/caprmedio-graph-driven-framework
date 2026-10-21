---
atom_id: CA-C-573
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
priority: high
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  concern_about: [CA-P-2536, CA-P-2550, CA-O-164, CA-R-1896, CA-M-352, CA-E-594]
version: 1
updated_at: "2026-10-21T16:54:03Z"
---
# Summary

Diagnose an unstarted selected-workflow dispatch

## Concern

The selected-workflow cleanup-problem Run `local-release-cleanup-problem-20261021-01`
reached `ENQUEUED` and was later cancelled after guarded observation. No execution
or effect is observed for this Run, and no child Run was created. The available
`worker.json`/`worker.ready` evidence is stale from 2026-10-16 while the observed
queue event is from 2026-10-21. This establishes an unstarted Run and a pending
liveness or deployment-observability gap; it does not establish that no worker
process exists anywhere, a software defect, or a worker fix.

CA-R-1896, CA-M-352 and CA-E-594 are the nearest existing release-host-worker
requirement, method and evaluation authorities; this Problem records a bounded
reconciliation gap and does not infer that their existing stop/observe paths cover
the unstarted queue item. The purpose-built `get_selected_workflow_run` observation
is authoritative for this exact Run; generic `get_execution_status` is RMED-only
and is not a new transport finding.

## Required boundary

Keep the exact queue/cancellation evidence and inspect the smallest applicable
worker-dispatch, deployment, and status authorities before proposing any repair.
Do not start a shared worker, drain unrelated jobs, replay the cancelled Run, or
infer that the installed Local release was affected. The active production MCP
container remains separately observed and is not evidence that this queued cleanup
Run executed.

## Blast radius

Selected-workflow cleanup ownership, worker readiness evidence, queue status
interpretation, and future deployment diagnostics. Preserve the actual
installed-adoption receipt, foreign resources, and all cancellation safeguards. No
Docker mutation, code change, release retry, or whole-Epic closure is authorized by
this Problem.
