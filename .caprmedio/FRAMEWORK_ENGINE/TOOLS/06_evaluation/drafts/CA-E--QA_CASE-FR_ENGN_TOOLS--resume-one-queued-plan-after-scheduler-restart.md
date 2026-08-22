---
subject_scopes:
  - tool-orchestration
  - failure-recovery
version: 1
updated_at: 2026-08-22 02:15:57
relations: {}
---
# Resume one queued plan after Scheduler restart

Given a persisted execution graph whose first step completed and whose declared second step is ready, terminate the Scheduler before dispatch and start a new Scheduler instance. Verify that it reconstructs readiness from Runtime state, claims the second step once, preserves the original action and step identities, and reaches the declared terminal result without asking a manager to recreate context.

Candidate alignment: CA-E-001, CA-E-002, CA-R-827, CA-R-861.

## Sources

- [Python documentation: queues](https://docs.python.org/3.14/library/asyncio-queue.html)
- [Python documentation: SQLite transaction control](https://docs.python.org/3/library/sqlite3.html#transaction-control)
