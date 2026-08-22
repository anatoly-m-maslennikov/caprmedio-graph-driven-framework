---
subject_scopes:
  - commit-automation
  - tool-orchestration
version: 1
updated_at: 2026-08-22 02:30:28
relations: {}
---
# Process automatic commits through durable single-flight scheduling

Treat a Codex Hook event as a wake-up and provenance observation, not as the governed file-change context. Atomically enqueue one immutable schema-versioned event under `.caprmedio_runtime/state/commit_automation/inbox/`, acknowledge only after that durability boundary, and let a repository-local background service reconcile the current Git-admitted repository frontier. Add low-frequency reconciliation so external editors, cancelled Hooks, and service downtime cannot make Hook delivery the correctness boundary.

Give `COMMIT_AUTOMATION` one deterministic I/O-free manager. From typed queue, repository, action, worker-result, settings, lease, and circuit facts, it returns exactly one admissible command. A mechanical Scheduler persists the transition and dispatches only that command. Enforce one active Git-mutating pipeline per repository; later events mark the repository pending and cause another reconciliation after the current action reaches a safe terminal state. Preserve every contributing event identity and session provenance even when an explicitly declared grouping policy coalesces events into one repository frontier.

Advance the fixed peer-Tool pipeline `COMMIT_CONTEXT` → `APPEND_CHANGE_RECORDS` → `COMMIT_CHANGE_SET`. `COMMIT_CHANGE_SET` owns only the final sealed Git mutation and must not import or orchestrate its peer Tools. Git Hooks remain independent Evaluations or observers and never drive this pipeline.

Persist recoverable transitions through `queued`, `reconciling`, `context_sealed`, `journaled`, `committing`, and `completed` or `no_change`, with explicit `retry_wait`, `paused`, `blocked`, and `dead_letter` outcomes from safe phases. Bind every transition to the action, installed release, input and result digests, attempt, diagnostics, worker result, and admissible next transitions. Recovery resumes from persisted state rather than blindly replaying the entire chain.

Candidate alignment: CA-R-004, CA-R-827, CA-R-846, CA-R-861, CA-M-002, CA-M-003, CA-M-005, CA-D-001, CA-E-002.

## Sources

- [Codex hooks documentation](https://learn.chatgpt.com/docs/hooks)
- [Python documentation: queues](https://docs.python.org/3.14/library/asyncio-queue.html)
- [Python documentation: SQLite transaction control](https://docs.python.org/3/library/sqlite3.html#transaction-control)
- [Git documentation: githooks](https://git-scm.com/docs/githooks)
