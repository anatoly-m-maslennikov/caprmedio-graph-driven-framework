---
atom_id: CA-E-595
ref_id: CA-E-595
container:
  scope_unit: CA-SU-27
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution
    Control
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control/Effect
    Authorization
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Component
    Structure
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation/Code
  - Subject/CAPRMEDIO/Carrier
tier: 6
relations:
  evaluation_for:
  - CA-R-1896
  - CA-M-352
  - CA-D-590
status: Archived
version: 18
updated_at: 2026-11-09 15:54:30 +0400
carrier_destination:
  file:
    name: CA-E-595@18-FRAMEWORK_DELIVERY-EVAL_CASE--verify-private-release-host-worker-shutdown.md
    path: .caprmedio_caprmedio/CA-SU-27_LAYER_5_FRAMEWORK_DELIVERY/06_evaluation/archive/retired_workflow_orchestrator
current_scope_unit: FRAMEWORK_DELIVERY
author: Anatoly Maslennikov
---

## Summary

verify private Release Host worker shutdown

## Claim

### Prose Claim

the Evaluation **must** verify that private shutdown stops only one exact idle host worker and proves its termination without changing work, history or another executor.

## Details

### Scope

the explicit `stop-release-worker` capability for an existing Release Host worker.

- submit one exact live ready identity and fresh shutdown nonce; verify acknowledgement precedes teardown but cannot claim stopped, and verify that current-code fingerprint drift still admits the matching live ready/worker record.
- alter each identity value, use a stale ready carrier, replay or alter a nonce, add an unknown key, exceed 4096 bytes, use a symlink or expire the deadline; verify refusal before Queue change, DBOS action, listener stop, metadata replacement or receipt.
- deny access to a shutdown carrier or its lock and verify closed refusal without a signal, arbitrary PID action or fallback executor.
- place PENDING or ENQUEUED host Queue work, including active or unknown queued work from any host application version, across the shared admission fence with `enqueue_selected` and `recover_selected_release`; verify busy refusal, no DBOS cancel/recovery/replay and no shutdown receipt.
- for an idle worker, verify dispatch closes at the fence; exact `stopping` metadata precedes listener join; listeners join before DBOS destroy; DBOS destroy precedes exact stopped metadata; the singleton lock releases before the final stopped receipt and CLI exit.
- force unproven listener join and verify stopping/unknown evidence remains, DBOS is not destroyed and no false stopped metadata, lock-release proof or stopped receipt is published.
- verify native and Docker Queues, existing Release Runs, canonical Journal facts, Unit effects, promotion and retirement remain unchanged; shutdown starts no worker and creates no Run.
- use a worker without shutdown IPC and verify bounded thirty-second `pending` or `unsupported` result with no signal/PID fallback; after upgrade, require a fresh request and identity rather than admitting the timed-out request.
- accept shutdown while withholding matching stopped metadata or singleton-lock release through the deadline; verify `pending`, exit 3, no final receipt, retry, force, DBOS cancellation or false stopped claim.
- verify requests and replies never exceed 4096 bytes, at most 64 pending requests are admitted, and no accepted, busy, pending or unsupported result is reported as stopped.
