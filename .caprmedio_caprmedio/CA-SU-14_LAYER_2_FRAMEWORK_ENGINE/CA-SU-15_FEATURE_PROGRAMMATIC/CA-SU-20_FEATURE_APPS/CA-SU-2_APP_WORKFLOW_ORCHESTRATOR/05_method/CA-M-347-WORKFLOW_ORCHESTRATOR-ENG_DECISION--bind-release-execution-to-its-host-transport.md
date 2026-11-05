---
atom_id: CA-M-347
ref_id: CA-M-347
role: Method
current_scope_unit: WORKFLOW_ORCHESTRATOR
status: Active
author: Anatoly Maslennikov
version: 17
updated_at: 2026-10-27 19:59:42 +0400
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Component Structure
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation/Code
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Effect Authorization
relations:
  method_for:
  - CA-R-1891
form: Eng Decision
tier: 4
container:
  scope_unit: CA-SU-2
carrier_destination:
  file:
    name: CA-M-347-WORKFLOW_ORCHESTRATOR-ENG_DECISION--bind-release-execution-to-its-host-transport.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-2_APP_WORKFLOW_ORCHESTRATOR/05_method
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
