---
subject_scopes:
  - python-engineering
version: 2
updated_at: 2026-08-22 01:50:50
relations: {}
---
# Centralize Tool decisions in one pure manager

Give each Tool one manager that owns all business logic and every decision about targets, ordering, fallback, retry, acceptance, and the next or final action. Make the manager deterministic and free of filesystem, process, clock, environment, network, logging-export, and persistence I/O; provide all observations and settings as explicit typed inputs and return a complete typed result or execution plan.

Assign each worker exactly one atomic mechanical operation. A worker performs no semantic choice and returns typed facts or a completion event. The manager defines the execution graph; a mechanical scheduler or direct dispatcher advances only transitions already named by that graph. A worker may directly invoke a fixed downstream worker or publish completion that makes the downstream step ready, but it must not select, reorder, skip, or invent another action.

Use a direct call for a short synchronous transition when it is sufficient and cheaper than durable scheduling. Use a runtime-owned queue when work must survive interruption, wait for dependencies, apply backpressure, or retry independently. A long-running worker that must survive manager termination must be registered and independently supervised as a background service; manager termination alone must not terminate that service.

Candidate alignment: CA-M-002, CA-M-005, CA-D-001, CA-D-002, CA-R-861.

## Sources

- [Python Functional Programming HOWTO](https://docs.python.org/3/howto/functional.html)
- [Python documentation: data classes](https://docs.python.org/3/library/dataclasses.html)
- [PEP 544 — Protocols](https://peps.python.org/pep-0544/)
- [Python documentation: `subprocess`](https://docs.python.org/3/library/subprocess.html)
- [Python documentation: queues](https://docs.python.org/3.14/library/asyncio-queue.html)
