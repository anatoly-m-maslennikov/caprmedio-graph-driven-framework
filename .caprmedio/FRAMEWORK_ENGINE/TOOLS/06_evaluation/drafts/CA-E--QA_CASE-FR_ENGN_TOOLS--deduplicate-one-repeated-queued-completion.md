---
subject_scopes:
  - tool-orchestration
  - failure-recovery
version: 1
updated_at: 2026-08-22 02:15:57
relations: {}
---
# Deduplicate one repeated queued completion

Given two identical completion deliveries for one action and step identity, process both through the Scheduler. Verify that the first advances the declared graph once, the second is recognized as already applied, and no downstream worker, mutation, or terminal record is duplicated.

Candidate alignment: CA-E-001, CA-E-002, CA-M-002, CA-R-827, CA-R-861.

## Sources

- [Python documentation: SQLite transaction control](https://docs.python.org/3/library/sqlite3.html#transaction-control)
- [Python documentation: sqlite3 integrity errors](https://docs.python.org/3/library/sqlite3.html#sqlite3.IntegrityError)
