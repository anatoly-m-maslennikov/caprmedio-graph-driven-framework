---
subject_scopes:
  - tool-orchestration
version: 1
updated_at: 2026-08-22 02:15:57
relations: {}
---
# Reject an undeclared downstream transition

Given a completed worker result that names a downstream step absent from the sealed execution graph, submit the result to both the direct dispatcher and queued Scheduler boundaries. Verify that each rejects the transition, dispatches no worker, records a stable diagnostic, and leaves the accepted graph unchanged.

Candidate alignment: CA-E-001, CA-E-002, CA-M-002, CA-R-861.

## Sources

- [Python documentation: queues](https://docs.python.org/3.14/library/asyncio-queue.html)
- [Python documentation: exceptions](https://docs.python.org/3/tutorial/errors.html)
