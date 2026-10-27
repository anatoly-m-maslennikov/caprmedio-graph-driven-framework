---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: Subject/Graph Node/Engineering/Execution Control/Recovery
  depends_on:
  - Subject/Graph Node/Implementation/Code/Tool
  - Subject/Graph Node/Engineering/Execution Control
version: 16
updated_at: 2026-10-27 06:04:45 +0400
relations: {}
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
content_role: Requirement
current_scope_unit: CORE_EXTENSIONS
status: Active
author: Anatoly Maslennikov
atom_id: CA-R-1480
type: Rule
tier: 1
---
# Keep triggered FPF work off the command-host path

**every** Hook-triggered **or** deferred FPF action **must** synchronously perform **only** bounded validation **and** durable idempotent intake **before** returning **to** the command host, **after** which the existing project-local asynchronous manager **and** Scheduler **must** dispatch isolated workers; the manager **must not** perform domain work **or** create one worker per Hook event, **and** the service **must** expose responsive manual `status`, `stop`, `start`, **and** `reload` controls plus bounded automatic timeout, heartbeat, retry, quarantine, restart, **and** circuit-breaker behavior while preserving accepted work **and** effect gates.
