---
atom_id: CA-D-583
ref_id: CA-D-583
container:
  scope_unit: CA-SU-27
role: Delivery
form: Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution
    Control
  dependencies:
  - Subject/CAPRMEDIO/Carrier
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Storage/Directory Layout
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation/Code
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
tier: 5
relations:
  delivery_for:
  - CA-R-1891
  - CA-M-347
status: Active
version: 15
updated_at: 2026-11-09 15:54:30 +0400
carrier_destination:
  file:
    name: CA-D-583-FRAMEWORK_DELIVERY-DECISION--store-release-host-state-in-an-isolated-namespace.md
    path: .caprmedio_caprmedio/CA-SU-27_LAYER_5_FRAMEWORK_DELIVERY/07_delivery
current_scope_unit: FRAMEWORK_DELIVERY
author: Anatoly Maslennikov
---

## Summary

store Release host state in an isolated namespace

## Claim

### Prose Claim

the Host Executor's mutable state Carriers **must** use `.caprmedio_install/workflow_orchestrator/release-host/`, separate from the native **and** Docker scheduler stores.

## Details

### Scope

the Release Host Executor's scheduler **and** transport-state Carriers in WORKFLOW_ORCHESTRATOR.

- the admitted runtime namespace value is `release-host`.
- the namespace contains its own database, worker lock, worker readiness, log, exact transport marker **and** private `health/requests/` and `health/replies/` Carriers.
- while holding the singleton worker lock, startup atomically publishes `worker.json` with exactly `pid`, lowercase-64-hex `start_token`, `application_version`, lowercase-64-hex `runtime_fingerprint` and `state: starting`; this state is not admitted. the health listener starts after DBOS initialization and before atomically publishing `worker.json` and `worker.ready` with those same five keys and `state: ready`. teardown stops and joins the listener before removing readiness.
- each health request and reply uses fixed `health/requests/<nonce>.json` and `health/replies/<nonce>.json` paths, where `nonce` is fresh lowercase-64-hex. both are atomic regular files no larger than 4096 bytes and have exactly `nonce`, `deadline_monotonic`, `pid`, `start_token`, `application_version`, `runtime_fingerprint` and `state`; `deadline_monotonic` is finite numeric monotonic time no later than request publication plus two seconds. symlinks, stale files and malformed content are rejected. request and reply bind the same seven values and `state: ready`.
- the channel permits at most 64 pending requests and fails closed beyond that bound. it is a private readiness Carrier only: it exposes no public Tool or HTTP endpoint and does not start workers, launch DBOS, schedule a Workflow, change a Queue, write Journal facts or execute effects.
- a per-Run binding carries the requested Run ID, frozen request digest **and** `release-host` transport identity.
- marker **and** binding publication are atomic; malformed, conflicting **or** symlinked state is rejected.
- the host scheduler has its own application **and** Queue identities. no existing Queue is copied **or** migrated.
- scheduler state remains transport evidence. actual Workflow, Step **and** Action facts remain in the existing canonical Journal.
