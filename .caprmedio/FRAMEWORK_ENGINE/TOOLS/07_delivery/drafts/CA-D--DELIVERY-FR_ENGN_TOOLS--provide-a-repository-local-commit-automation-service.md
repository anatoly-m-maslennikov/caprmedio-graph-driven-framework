---
subject_scopes:
  - commit-automation
  - tool-orchestration
version: 1
updated_at: 2026-08-22 02:30:28
relations: {}
---
# Provide a repository-local commit automation service

Deliver `COMMIT_AUTOMATION` as one independently supervised repository-local background Tool service. It consumes the durable event inbox, reconciles the current Git-admitted repository frontier, asks one pure manager for the next admissible command, persists every state transition, and lets a mechanical Scheduler dispatch the fixed peer-Tool pipeline `COMMIT_CONTEXT` → `APPEND_CHANGE_RECORDS` → `COMMIT_CHANGE_SET`.

Deliver one repository lease and one active Git-mutating pipeline. Keep new events durable and mark the repository pending while a pipeline is active. Preserve every contributing event identity when events are grouped under an explicitly declared policy. Add low-frequency reconciliation so the service detects missed Hook delivery and external project edits without attributing repository truth to one host callback.

Persist schema-versioned action state under `.caprmedio_runtime/state/commit_automation/`, including phase, action and event identities, selected installed release, input and result digests, attempt, lease, worker result, diagnostics, next admissible transitions, circuit state, and terminal receipt. Before Journal acceptance, the durable inbox may carry the minimum host provenance needed to survive Hook or service failure. After acceptance, retain only Journal-resolvable identities and receipts. Keep Runtime state reconstructible, non-authoritative, and outside Git. Keep each peer Tool independently invocable; the service owns scheduling, while the final Git Doer owns only its sealed mutation boundary.

Candidate alignment: CA-R-004, CA-R-827, CA-R-846, CA-R-861, CA-M-002, CA-M-003, CA-M-005, CA-D-001, CA-D-002, CA-E-002.

## Sources

- [Python documentation: queues](https://docs.python.org/3.14/library/asyncio-queue.html)
- [Python documentation: SQLite transaction control](https://docs.python.org/3/library/sqlite3.html#transaction-control)
- [Codex hooks documentation](https://learn.chatgpt.com/docs/hooks)
