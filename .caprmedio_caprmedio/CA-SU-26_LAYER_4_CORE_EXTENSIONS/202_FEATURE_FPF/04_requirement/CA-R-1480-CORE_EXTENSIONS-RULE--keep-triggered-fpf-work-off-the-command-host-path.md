---
cce_version: cce_1
cce_form: obligation
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Recovery
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation/Code/Tool
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control
version: 17
updated_at: 2026-10-27 19:59:55 +0400
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: CORE_EXTENSIONS
status: Active
author: Anatoly Maslennikov
atom_id: CA-R-1480
ref_id: CA-R-1480
tier: 1
role: Requirement
form: Rule
container:
  scope_unit: CA-SU-26
---
# Keep triggered FPF work off the command-host path

**every** Hook-triggered **or** deferred FPF action **must** synchronously perform **only** bounded validation **and** durable idempotent intake **before** returning **to** the command host, **after** which the existing project-local asynchronous manager **and** Scheduler **must** dispatch isolated workers; the manager **must not** perform domain work **or** create one worker per Hook event, **and** the service **must** expose responsive manual `status`, `stop`, `start`, **and** `reload` controls plus bounded automatic timeout, heartbeat, retry, quarantine, restart, **and** circuit-breaker behavior while preserving accepted work **and** effect gates.
