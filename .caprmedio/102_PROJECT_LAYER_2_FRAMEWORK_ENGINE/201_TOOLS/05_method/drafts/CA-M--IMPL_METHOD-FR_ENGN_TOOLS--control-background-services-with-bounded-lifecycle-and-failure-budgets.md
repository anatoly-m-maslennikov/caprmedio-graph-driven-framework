---
subject_scopes:
  - background-services
  - failure-recovery
version: 1
updated_at: 2026-08-22 02:30:28
relations: {}
---
# Control background services with bounded lifecycle and failure budgets

Give every registered background service one inspectable lifecycle interface: `status`, `pause`, `resume`, `stop`, `start`, and `reload`. Keep admission, queued work, active work, installed release, process identity, leases, last result, diagnostics, circuit state, and dead letters distinct. Preserve durable queue and action state through every lifecycle command.

`pause` stops new dispatch while intake may remain available. `stop` stops admission and reaches a declared safe shutdown boundary without deleting queued work. `start` resumes admission and drains accepted work. `reload` reaches a safe boundary, re-resolves the selected installed release, restarts, and reconciles preserved work. Use cooperative cancellation and bounded shutdown; never force termination across a declared mutation critical section whose authoritative state is not yet recoverable.

Declare separate queue-count, queue-byte, worker-timeout, lease, crash, consecutive-failure, cooldown, restart, and recovery budgets only after measuring the applicable execution surface. Open the circuit and pause autonomous dispatch when a budget is exhausted or a check is `violated`, `unknown`, or `error`. A supervisor may restart a crashed service only inside its restart budget. Automatically resume only a classified transient failure before governed mutation after its cooldown and health check pass; governance, Journal, staging, ambiguous Git, and lease-integrity failures require explicit Operator recovery.

Use structured task ownership, explicit cancellation, and visible child-failure propagation only when the service has genuinely concurrent related work. Keep the repository-local service portable; isolate any later host-native supervisor behind a replaceable adapter.

Candidate alignment: CA-R-004, CA-R-815, CA-R-827, CA-R-846, CA-R-861, CA-M-003, CA-M-005, CA-D-001, CA-D-002, CA-E-002.

## Sources

- [Python documentation: asyncio task groups](https://docs.python.org/3.14/library/asyncio-task.html#task-groups)
- [Python documentation: subprocess](https://docs.python.org/3.14/library/subprocess.html)
- [Python documentation: signal handling](https://docs.python.org/3/library/signal.html)
