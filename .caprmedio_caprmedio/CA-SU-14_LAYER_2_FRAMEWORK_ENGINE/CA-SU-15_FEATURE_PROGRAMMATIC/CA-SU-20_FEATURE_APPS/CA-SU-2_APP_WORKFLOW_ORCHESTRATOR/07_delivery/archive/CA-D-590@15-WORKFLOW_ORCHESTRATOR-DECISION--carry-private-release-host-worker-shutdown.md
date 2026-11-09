---
atom_id: CA-D-590@15
ref_id: CA-D-590@15
container:
  scope_unit: CA-SU-2
role: Delivery
form: Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution
    Control
  dependencies:
  - Subject/CAPRMEDIO/Carrier
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control/Effect
    Authorization
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Component
    Structure
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation/Code
tier: 5
relations:
  delivery_for:
  - CA-R-1896
  - CA-M-352
status: Archived
version: 15
updated_at: 2026-11-09 07:45:14 +0400
carrier_destination:
  file:
    name: CA-D-590@15-WORKFLOW_ORCHESTRATOR-DECISION--carry-private-release-host-worker-shutdown.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-2_APP_WORKFLOW_ORCHESTRATOR/07_delivery/archive
current_scope_unit: WORKFLOW_ORCHESTRATOR
author: Anatoly Maslennikov
---

## Summary

carry private Release Host worker shutdown

## Claim

### Prose Claim

the Delivery **must** carry shutdown only through a closed private IPC contract that binds one ready identity and nonce, distinguishes acceptance from proven stop, and exposes no signal or arbitrary-PID operation.

## Details

### Scope

the fixed `stop-release-worker` command and shutdown request, acknowledgement and final receipt Carriers below the Release Host namespace.

- use only `.caprmedio_install/workflow_orchestrator/release-host/shutdown/requests/<nonce>.json`, `shutdown/replies/<nonce>.json`, `shutdown/admission.lock` and `shutdown/stopping.json`. Carriers are atomic regular files, never symlinks, each at most 4096 bytes; at most 64 pending requests are admitted. The shared `admission.lock` serializes shutdown admission with `enqueue_selected` and `recover_selected_release`.
- the request has exactly `operation`, `nonce`, `deadline_monotonic`, `pid`, `start_token`, `application_version`, `runtime_fingerprint`, `state`, where `operation: stop-release-worker`, `state: ready`, nonce/token/fingerprint are lowercase-64-hex, pid is positive, and deadline is finite monotonic time no later than thirty seconds after publication.
- an acknowledgement has exactly the request keys plus `disposition`. It is `accepted` or `busy`; `accepted` is only shutdown admission and does not claim stopped. A busy acknowledgement preserves the ready worker and carries no stop receipt.
- `shutdown/stopping.json` has exactly `nonce`, `pid`, `start_token`, `application_version`, `runtime_fingerprint`, `state`, where `state: stopping` and every identity value equals the accepted request. It is written before listener join. On unproven join it remains the only shutdown state: DBOS stays live and neither stopped metadata nor a final receipt is written.
- the final stopped receipt replaces the accepted acknowledgement only after foreground exit releases the singleton lock. It has exactly `operation`, `nonce`, `pid`, `start_token`, `application_version`, `runtime_fingerprint`, `state`, `disposition`, `lock_released`, where `state: stopped`, `disposition: stopped` and `lock_released: true`; its identity exactly matches the prior request and final worker metadata.
- the command's nonterminal local JSON outputs have exactly `operation`, `nonce`, `disposition`: `busy`, `pending` or `unsupported`. Their process exit codes are respectively 2, 3 and 4; only the final stopped receipt exits 0 and carries verified identity. The command waits no more than thirty seconds for acknowledgement and final proof. A missing acknowledgement, or accepted acknowledgement without both matching stopped metadata and singleton-lock release by that deadline, is `pending` with exit 3 and no final receipt, retry or force; a proved older protocol is `unsupported`; neither is a reply that claims stopped. The command authenticates exact matching ready and worker records through `probe_worker`, not current-code availability, and does not use health files to activate shutdown, signals, arbitrary PIDs, DBOS cancel/recovery, a fallback worker or a new Run.
