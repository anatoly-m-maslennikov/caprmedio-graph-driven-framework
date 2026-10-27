---
atom_id: CA-P-942@4
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
subjects:
  governs: Subject/Engineering/Skill
  depends_on:
  - Subject/Engineering/Tool
  - Subject/Engineering/Carrier
  - CA Main Skill Runtime Closure Validation
  - CA-P-941
version: 4
updated_at: 2026-10-24 07:20:19 +0400
autonomous_confidence_threshold: 99
relations: {}
status: Archived
current_scope_unit: caprmedio
content_role: Plan
type: Plan
label: Task
tier: 3
---
# Validate CA Main Skill Runtime Closure

**when** CA-P-941 is Done, **then** the Assignee **must** validate the installed CA Main Skill vertical slice from Codex host invocation through routing, asynchronous execution, lifecycle control, effect gating, durable receipt, and recovery.

## Scope

`((installed CA Main Skill vertical slice) union (fresh Codex runtimes) union (static, negative, fault-injection, concurrency, recovery, compaction, idempotency, approval, and end-to-end evidence))`

## Definition of Done

the Task is **not done if** (fresh Codex `$ca` invocations do not select the expected canonical route and Tool contract **or** an unregistered, ambiguous, stale, or unauthorized request succeeds **or** a Hook or trigger blocks an unrelated command such as `pwd` beyond its bounded submission timeout **or** a hung worker makes manager controls unresponsive **or** manual or automatic stop, start, reload, circuit-breaker, and recovery behavior is unproved **or** compaction or restart loses the pinned authority snapshot, job state, approval state, idempotency boundary, or durable receipt **or** an interrupted effect is duplicated **or** static validation, installation proof, process-state proof, and runtime-behavior proof are conflated **or** any required test or fresh-runtime scenario fails).

## Details

keep Claude runtime validation and cross-host equivalence testing outside this Task under the host-support boundary established by CA-P-936. record separate receipts for source validation, installation, service state, each host invocation, asynchronous state transitions, lifecycle-control actions, effects, and reconciliation. include a regression that proves command-host dispatch remains responsive while CA work is queued, running, stopped, failed, and reloaded.
