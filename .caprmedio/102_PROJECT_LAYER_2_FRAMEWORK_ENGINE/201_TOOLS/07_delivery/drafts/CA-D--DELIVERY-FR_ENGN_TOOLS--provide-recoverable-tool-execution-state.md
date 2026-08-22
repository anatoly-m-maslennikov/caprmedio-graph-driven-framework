---
subject_scopes:
  - tool-orchestration
  - failure-recovery
version: 1
updated_at: 2026-08-22 02:15:57
relations: {}
---
# Provide recoverable Tool execution state

Deliver a runtime-owned execution-plan carrier and Scheduler interface for Tool chains that require durable handoffs. Each plan records its action identity, immutable directed step graph, typed step contracts, dependency state, bounded retry routes, terminal states, and manager provenance. Each attempt records its step identity, lease, input and output digests, status, diagnostics, and completion identity.

The Scheduler claims only ready steps, advances only declared transitions, deduplicates repeated completion, and resumes from persisted state after interruption. Keep this reconstructible operational state in `.caprmedio_runtime`; it is not RMED authority and does not enter Git history. Permit direct typed handoffs to bypass the carrier when the plan is short, synchronous, and needs no independent recovery.

Candidate alignment: CA-D-001, CA-D-002, CA-M-002, CA-M-005, CA-R-827, CA-R-861.

## Sources

- [Python documentation: queues](https://docs.python.org/3.14/library/asyncio-queue.html)
- [Python documentation: SQLite transaction control](https://docs.python.org/3/library/sqlite3.html#transaction-control)
- [Python documentation: task groups](https://docs.python.org/3/library/asyncio-task.html#task-groups)
