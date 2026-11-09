---
atom_id: CA-R-1896
ref_id: CA-R-1896
container:
  scope_unit: CA-SU-27
role: Requirement
form: Rule
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
tier: 3
status: Active
version: 17
updated_at: 2026-11-09 15:54:30 +0400
carrier_destination:
  file:
    name: CA-R-1896-FRAMEWORK_DELIVERY-RULE--stop-an-idle-release-host-worker-through-private-ipc.md
    path: .caprmedio_caprmedio/CA-SU-27_LAYER_5_FRAMEWORK_DELIVERY/04_requirement
current_scope_unit: FRAMEWORK_DELIVERY
author: Anatoly Maslennikov
relations: {}
---

# Summary

stop an idle Release Host worker through private IPC

## Scope

the explicit `stop-release-worker` capability for one already started Release Host Executor in WORKFLOW_ORCHESTRATOR.

## Claim

WORKFLOW_ORCHESTRATOR **must** provide an explicit private shutdown capability that stops only an exactly identified, idle Release Host worker, while refusing busy, stale, unauthorized or unavailable targets without cancelling, replaying or transferring any Release work.

## Details

- the capability is explicit and Release-host-only; it addresses no arbitrary PID, sends no process signal and has no native or Docker fallback.
- admission requires the current closed ready identity `pid`, `start_token`, `application_version`, `runtime_fingerprint`, `state: ready`, plus one fresh request nonce. A stale or changed published identity is a refusal, not authority to stop a replacement worker; a live ready carrier and worker record with exact matching identity remain eligible even when their runtime fingerprint is stale against current code on disk, because shutdown may be needed to refresh that worker.
- the worker holds one race-free shutdown-admission fence before acknowledgement. It refuses whenever its host Queue has a PENDING or ENQUEUED item, including active work, and accepts no later dispatch once the fence is held.
- accepted shutdown is not evidence of stopped shutdown. The worker first quiesces, joins every private listener, then destroys DBOS, writes exact stopped metadata, and exits to release its singleton lock. The requesting CLI returns a final stopped receipt only after it proves the lock is released.
- shutdown starts no Worker, creates no Run, cancels no DBOS work, calls no recovery, replays no Workflow, writes no Journal gate or Release effect, and cannot justify promotion, retirement or another Release phase.
- an older worker that does not implement the shutdown IPC, or any request without its bounded acknowledgement, returns only a bounded pending or unsupported result and requires an upgrade; no signal or PID fallback is permitted.
