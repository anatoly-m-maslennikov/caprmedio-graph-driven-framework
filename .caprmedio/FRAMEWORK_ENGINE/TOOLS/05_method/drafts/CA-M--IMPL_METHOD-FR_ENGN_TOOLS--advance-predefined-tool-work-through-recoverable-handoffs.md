---
subject_scopes:
  - tool-orchestration
version: 1
updated_at: 2026-08-22 01:50:50
relations: {}
---
# Advance predefined Tool work through recoverable handoffs

Represent a multi-Tool action as a manager-produced directed execution graph. Give every step a stable action identity, step identity, typed input, declared dependencies, accepted output contract, and manager-defined success, failure, and bounded-retry transitions. A Tool completion enables only downstream steps already present in that graph; it does not decide what should happen next.

For short same-process work, pass the typed result directly to the fixed downstream Tool. When execution must survive interruption, wait, apply backpressure, or retry independently, persist the plan and step state in `.caprmedio_runtime` and let a mechanical scheduler claim and dispatch ready steps through a queue. Record attempts, leases, completion state, and diagnostics so the scheduler can deduplicate delivery and resume without inventing context.

Use idempotent operations where practical and an exclusive lease or equivalent compare-and-set boundary for non-repeatable effects. Reject undeclared cycles; model a retry as an explicit bounded transition with a terminal failure state. A worker or Tool may say “completed; this declared step is now ready,” but it may not select, reorder, or synthesize another step.

Candidate alignment: CA-M-002, CA-M-005, CA-D-001, CA-D-002, CA-R-861.

## Sources

- [Python documentation: queues](https://docs.python.org/3.14/library/asyncio-queue.html)
- [Python documentation: task groups](https://docs.python.org/3/library/asyncio-task.html#task-groups)
- [Python documentation: SQLite transaction control](https://docs.python.org/3/library/sqlite3.html#transaction-control)
