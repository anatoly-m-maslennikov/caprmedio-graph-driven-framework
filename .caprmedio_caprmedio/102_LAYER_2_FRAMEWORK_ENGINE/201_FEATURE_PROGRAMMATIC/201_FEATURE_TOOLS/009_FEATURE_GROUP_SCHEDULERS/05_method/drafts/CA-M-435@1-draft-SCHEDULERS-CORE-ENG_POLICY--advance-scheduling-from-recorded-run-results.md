---
atom_id: CA-M-435@1-draft
content_role: Method
type: Eng Policy
current_scope_unit: SCHEDULERS
claim_target_scope_unit: SCHEDULERS
tier: 1
status: Draft
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-23 18:22:28 +0400"
subjects:
  governs: "Subject/Engineering/Workflow Orchestration/Scheduling"
  depends_on: []
---
# Summary

Advance scheduling from recorded run results

## Scope

The SCHEDULERS children and their scheduling boundary inside the shared TOOLS
runtime.

## Claim

SCHEDULERS has two children: `BATCH_SCHEDULER` and `WORKFLOW_SCHEDULER`.
WORKFLOW_SCHEDULER orders steps and substeps. A parent with substeps makes no
`actionRun` calls; it only orders its substeps. Each leaf step or substep has
one `BatchActionRun`, and each batch contains >=1 `SingleActionRun`. The batch
scheduler submits jobs and aggregates results; the Action Engine executes and
records results. Results flow from Action Engine to Batch Scheduler to Workflow
Scheduler through shared persistent run state; there is no separate result
broker.

## Details

Scheduling is asynchronous and independent of the caller. Queue and run state
survive restart, with IDs, status, and reconnect available afterward. This
Method does not invent automatic retry, rollback, global locks, or same-process
transactional requirements.
