---
subject_scopes:
  - commit-automation
  - tool-orchestration
version: 1
updated_at: 2026-08-22 02:30:28
relations: {}
---
# Keep one commit-automation manager pure and deterministic

Given one complete typed queue, repository, action, worker-result, settings, lease, and circuit fact set, invoke the commit-automation manager repeatedly while replacing filesystem, process, clock, environment, network, logging-export, and persistence boundaries with failing sentinels. Verify every invocation returns the same typed command and admissible transitions, performs no I/O, and leaves every effect or observation to a worker or adapter.

The case fails on any boundary call, implicit state read, nondeterministic command, worker-selected transition, or output that does not completely identify the next admitted operation.

Candidate alignment: CA-E-001, CA-E-002, CA-M-002, CA-M-005, CA-D-001, CA-D-002.

## Sources

- [Python documentation: unittest.mock](https://docs.python.org/3/library/unittest.mock.html)
- [Python Functional Programming HOWTO](https://docs.python.org/3/howto/functional.html)
