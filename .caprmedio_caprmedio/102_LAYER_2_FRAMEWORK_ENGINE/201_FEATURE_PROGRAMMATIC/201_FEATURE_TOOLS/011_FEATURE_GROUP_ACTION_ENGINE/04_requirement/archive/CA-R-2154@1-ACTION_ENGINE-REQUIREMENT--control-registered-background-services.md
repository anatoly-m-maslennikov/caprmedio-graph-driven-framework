---
subjects:
  governs: Subject/Engineering/Tool//START_BACKGROUND_SERVICES
  depends_on: []
version: 1
updated_at: 2026-10-24 03:32:20 +0400
relations: {}
atom_id: CA-R-2154@1
status: Archived
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: ACTION_ENGINE
type: Rule
tier: 1
---
# Control registered background services

`START_BACKGROUND_SERVICES` is an `ACTION_ENGINE` runtime-control operation. It **must** read one machine-readable registry from the selected installed release **and** expose status, pause, resume, stop, start, **and** reload for **every** enabled service.

**every** command **must** preserve accepted inbox, queue, action, receipt, circuit, **and** dead-letter state. pause stops new dispatch **without** deleting accepted intake. stop stops admission **and** reaches a declared safe shutdown boundary. start resumes admission **and** drains accepted work. reload reaches a safe boundary, re-resolves the selected installed release, restarts, **and** reconciles preserved work. No command **may** force termination across an unrecoverable mutation critical section.

the Tool **must** use dry-run **unless** apply is explicit, treat an empty registry as a successful no-op, reject duplicate **or** unsafe declarations **before** mutation, permit Framework implementation **only** from `.caprmedio_runtime/tools`, write persistent operational state **only** below `.caprmedio_runtime`, **and** write disposable process staging **and** cache state **only** below `.caprmedio_tmp`. Repeated apply **must** be idempotent. Automatic restart **and** retry **must** remain within declared measured budgets. Exhausted budgets, governance failures, Journal failures, staging failures, ambiguous Git outcomes, **and** lease-integrity failures **must** open the circuit **or** pause autonomous dispatch **and** require explicit Operator recovery.
