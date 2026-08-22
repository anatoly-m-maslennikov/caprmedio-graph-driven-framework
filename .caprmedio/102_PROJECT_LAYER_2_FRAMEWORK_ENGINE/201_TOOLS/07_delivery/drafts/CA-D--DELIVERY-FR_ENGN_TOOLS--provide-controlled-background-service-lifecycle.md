---
subject_scopes:
  - background-services
  - failure-recovery
version: 1
updated_at: 2026-08-22 02:30:28
relations: {}
---
# Provide controlled background-service lifecycle

Deliver one common lifecycle surface for registered background Tools with `status`, `pause`, `resume`, `stop`, `start`, and `reload`. Report the service and worker process identities, selected installed release, queue count and bytes, current action and phase, pending state, lease, last success and failure, failure-budget usage, circuit state, and dead-letter count without requiring Runtime-file inspection.

Preserve inbox, queue, and action state across every command. Stop and reload reach a declared safe boundary before process replacement; they do not delete accepted work or force termination across an unrecoverable mutation critical section. Automatic restart, cooldown, health checking, and resume remain bounded by explicit settings and failure classifications. Budget exhaustion leaves the service visibly paused or stopped for Operator action.

Keep platform-specific supervision behind a replaceable adapter and keep mutable process, log, lock, queue, circuit, and cache state below `.caprmedio_runtime`.

Candidate alignment: CA-R-004, CA-R-815, CA-R-827, CA-R-846, CA-R-861, CA-M-003, CA-M-005, CA-D-001, CA-D-002, CA-E-002.

## Sources

- [Python documentation: subprocess](https://docs.python.org/3.14/library/subprocess.html)
- [Python documentation: asyncio task groups](https://docs.python.org/3.14/library/asyncio-task.html#task-groups)
- [Python documentation: signal handling](https://docs.python.org/3/library/signal.html)
