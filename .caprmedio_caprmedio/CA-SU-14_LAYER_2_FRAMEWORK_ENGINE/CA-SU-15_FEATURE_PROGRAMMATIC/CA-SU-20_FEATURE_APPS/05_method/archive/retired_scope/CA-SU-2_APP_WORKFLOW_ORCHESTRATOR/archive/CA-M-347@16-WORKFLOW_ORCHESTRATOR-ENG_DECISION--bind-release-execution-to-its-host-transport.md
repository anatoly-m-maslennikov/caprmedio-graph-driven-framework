---
atom_id: CA-M-347@16
content_role: Method
current_scope_unit: WORKFLOW_ORCHESTRATOR
status: Archived
author: Anatoly Maslennikov
version: 16
updated_at: 2026-10-27 06:04:45 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Execution Control
  depends_on:
  - Subject/Graph Node/Engineering/Architecture/Communication
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Engineering/Architecture/Component Structure
  - Subject/Graph Node/Implementation/Code
  - Subject/Graph Node/Engineering/Execution Control/Effect Authorization
relations:
  method_for:
  - CA-R-1891
type: Eng Decision
tier: 4
---
# Summary

bind Release execution to its host transport

## Scope

transport selection for source-admitted Release Version Runs in WORKFLOW_ORCHESTRATOR.

## Claim

the Host Executor **must** bind **every** admitted Release Run **to** its exact frozen request **and** isolated host transport **before** scheduling it.

## Details

- validate the existing selected-route seals **and** current Source bindings **before** accepting a new Run.
- use the dedicated host Queue **and** worker; verify the frozen Release route again at worker dispatch.
- pass the fixed host namespace **to** the executor subprocess. do **not** change the MCP process's shared environment **to** select a transport.
- observation **and** recovery use the Run's retained transport binding. a Run bound **to** another executor is **not** adopted.
- unchanged requests can reuse their exact binding idempotently. a conflicting request, missing worker readiness **or** uncertain prior effect blocks continuation.
- ordinary host admission, status **and** recovery prove live readiness through the private host health exchange, not a signal probe. under the held singleton lock, startup creates one lowercase-64-hex `start_token`; the initial `worker.json` has closed identity `pid`, `start_token`, `application_version`, `runtime_fingerprint`, `state: starting` and is not admitted. after listener initialization, `worker.json` **and** `worker.ready` carry the same closed identity with `state: ready`.
- availability atomically publishes one private request keyed by a fresh lowercase-64-hex nonce. request and reply have exactly `nonce`, `deadline_monotonic`, `pid`, `start_token`, `application_version`, `runtime_fingerprint` and `state`; `deadline_monotonic` is finite numeric monotonic time no later than publication time plus two seconds. the initialized listener replies once with the same seven values before that deadline. only a fresh, metadata-matching `ready` reply admits ordinary work.
- missing, inaccessible, oversized, symlinked, malformed, stale, replayed or wrong-identity exchange blocks before a child, Queue, DBOS Workflow **or** effect. permission denial from a legacy signal observation is non-authoritative: it neither proves nor defeats a valid health exchange. the N15 fixed one-shot unknown-effect resolution remains its separately authorized exception.
