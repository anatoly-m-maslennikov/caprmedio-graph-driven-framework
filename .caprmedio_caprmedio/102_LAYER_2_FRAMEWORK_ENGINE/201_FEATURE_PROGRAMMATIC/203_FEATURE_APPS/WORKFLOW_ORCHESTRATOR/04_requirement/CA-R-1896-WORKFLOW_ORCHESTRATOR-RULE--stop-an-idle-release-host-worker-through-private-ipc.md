---
atom_id: CA-R-1896
content_role: Requirement
current_scope_unit: WORKFLOW_ORCHESTRATOR
status: Active
author: Anatoly Maslennikov
version: 15
updated_at: 2026-10-27 06:04:45 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Execution Control
  depends_on:
  - Subject/Graph Node/Engineering/Architecture/Communication
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Engineering/Execution Control/Effect Authorization
  - Subject/Graph Node/Engineering/Architecture/Component Structure
  - Subject/Graph Node/Implementation/Code
  - Subject/Graph Node/Carrier
relations: {}
tier: 3
type: Rule
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
