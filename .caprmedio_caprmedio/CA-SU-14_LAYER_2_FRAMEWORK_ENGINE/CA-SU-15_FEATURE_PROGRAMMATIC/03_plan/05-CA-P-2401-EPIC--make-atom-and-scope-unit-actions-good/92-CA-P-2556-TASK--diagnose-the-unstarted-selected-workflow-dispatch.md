---
atom_id: CA-P-2556
ref_id: CA-P-2556
container:
  atom: CA-P-2401
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Engineering/Workflow Orchestration/Run Execution Dispatch
tier: 3
relations:
  is_decomposition_of:
  - CA-P-2401
status: Backlog
version: 5
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 92-CA-P-2556-TASK--diagnose-the-unstarted-selected-workflow-dispatch.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/03_plan/5-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/001_backlog
work_sequence_number: 92
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
# Summary

Diagnose the unstarted selected-workflow dispatch

## Objective

Bound the liveness and deployment-observability gap raised by CA-C-573 without
starting a shared worker, draining unrelated jobs, replaying the canceled Run, or
claiming a software defect or fix.

## Details

At most 15 minutes own work. Inspect the exact queue/cancellation evidence for
`local-release-cleanup-problem-20261021-01`, the stale `worker.json`/
`worker.ready` evidence, and the current applicable worker/deployment authorities.
Use the purpose-built `get_selected_workflow_run` result for this exact Run and
preserve that generic `get_execution_status` is RMED-only. Separate the unstarted
selected-workflow Run from the actual installed Local release and its healthy
production MCP container. Root owns worker process control, Git, Docker, runtime,
and any deployment effect; this Task is read-only planning/diagnosis.

### Definition of Done

Record the exact observed queue state, worker-readiness evidence, applicable
authority, and next bounded action. If the cause remains uncertain, keep CA-C-573
Active and this Task Backlog. No worker start, queue drain, replay, release retry,
or whole-Epic closure is implied.
