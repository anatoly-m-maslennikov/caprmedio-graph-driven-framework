---
subject_scopes:
  - background-services
  - failure-recovery
version: 1
updated_at: 2026-08-22 02:30:28
relations: {}
---
# Preserve queued work through service lifecycle controls

Given one queued action, one active safe-phase worker, and one newly selected installed release, invoke `pause`, `resume`, `stop`, `start`, and `reload` in sequence. Verify intake and dispatch follow each declared command, the queue and action identities remain intact, stop reaches a safe boundary, start drains accepted work, reload selects the new verified release only after the safe boundary, and status reports every transition without deleting evidence.

The case fails on lost or duplicated work, forced termination across an unrecoverable mutation boundary, stale release execution after reload, hidden process state, or a lifecycle command that edits governed source.

Candidate alignment: CA-E-001, CA-E-002, CA-R-004, CA-R-827, CA-R-846, CA-R-861.

## Sources

- [Python documentation: subprocess](https://docs.python.org/3.14/library/subprocess.html)
- [Python documentation: signal handling](https://docs.python.org/3/library/signal.html)
